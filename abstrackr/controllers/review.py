import pdb
import os
import shutil
import datetime

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
import logging
from repoze.what.predicates import not_anonymous, has_permission
from repoze.what.plugins.pylonshq import ActionProtector
from abstrackr.lib.base import BaseController, render
import abstrackr.model as model
from pylons import request, response, session, tmpl_context as c, url
from abstrackr.lib import xml_to_sql
# this is the path where uploaded databases will be written to
permanent_store = "/uploads/"

log = logging.getLogger(__name__)

class ReviewController(BaseController):

    @ActionProtector(not_anonymous())
    def create_new_review(self):
        return render("/reviews/new.mako")
    
    @ActionProtector(not_anonymous())
    def create_review_handler(self):
        # first upload the xml file
        xml_file = request.params['db']
        local_file_path = "." + os.path.join(permanent_store, 
                          xml_file.filename.lstrip(os.sep))
        local_file = open(local_file_path, 'w')
        
        shutil.copyfileobj(xml_file.file, local_file)
        xml_file.file.close()
        local_file.close()
        
        current_user = request.environ.get('repoze.who.identity')['user']
        new_review = model.Review()
        new_review.name = request.params['name']
        new_review.project_lead_id = current_user.id
        new_review.project_description = request.params['description']
        new_review.date_created = datetime.datetime.now()
        model.Session.add(new_review)
        model.Session.commit()
        
        # now parse the uploaded file
        print "parsing uploaded xml..."
        xml_to_sql.xml_to_sql(local_file_path, new_review)
        print "done."
        
        redirect(url(controller="review", action="show_review", id=new_review.review_id))       
        
    @ActionProtector(not_anonymous())
    def join_a_review(self):
        review_q = model.meta.Session.query(model.Review)
        c.all_reviews = review_q.all()
        return render("/reviews/join_a_review.mako")
        
      
    @ActionProtector(not_anonymous())
    def show_review(self, id):
        review_q = model.meta.Session.query(model.Review)
        c.review = review_q.filter(model.Review.review_id == id).one()
        # grab all of the citations associated with this review
        citation_q = model.meta.Session.query(model.Citation)
        citations_for_review = citation_q.filter(model.Citation.review_id == id).all()
   
        c.num_citations = len(citations_for_review)
        # and the labels provided thus far
        label_q = model.meta.Session.query(model.Label)
        ### TODO first of all, will want to differentiate between
        # unique and total (i.e., double screened citations). will
        # also likely want to pull additional information here, e.g.,
        # the participating reviewers, etc.
        labels_for_review = label_q.filter(model.Label.review_id == id).all()
        c.num_labels = len(labels_for_review)
        return render("/reviews/show_review.mako")
          
    @ActionProtector(not_anonymous())
    def join_review(self, id):
        current_user = request.environ.get('repoze.who.identity')['user']
        # for now just adding right away; may want to 
        # ask project lead for permission though.
        reviewer_project = model.ReviewerProject()
        reviewer_project.reviewer_id = current_user.id
        reviewer_project.review_id = id
        model.Session.add(reviewer_project)
        model.Session.commit()
        redirect(url(controller="account", action="welcome"))  
    