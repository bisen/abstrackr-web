# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291154720.3440001
_template_filename='C:\\dev\\abstrackr_web\\abstrackr\\abstrackr\\templates/citation_fragment.mako'
_template_uri='/citation_fragment.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n<h2>')
        # SOURCE LINE 2
        __M_writer(escape(c.cur_citation.marked_up_title))
        __M_writer(u'</h2>\r\n')
        # SOURCE LINE 3
        __M_writer(escape(c.cur_citation.authors))
        __M_writer(u'<br/><br/>\r\n')
        # SOURCE LINE 4
        __M_writer(escape(c.cur_citation.marked_up_abstract))
        __M_writer(u'\r\n\r\n<script type="text/javascript">\r\n\r\n        function markup_current(){\r\n            // reload the current citation, with markup\r\n            $("#wait").text("marking up the current citation..")\r\n            $("#citation").fadeOut(\'slow\', function() {\r\n                $("#citation").load("')
        # SOURCE LINE 12
        __M_writer(escape('/markup/%s/%s' % (c.review_id, c.cur_citation.citation_id)))
        __M_writer(u'", function() {\r\n                     $("#citation").fadeIn(\'slow\');\r\n                     $("#wait").text("");\r\n                });\r\n            });\r\n        }\r\n    \r\n    \r\n        $("#accept").click(function() {\r\n            $("#wait").text("hold on to your horses..")\r\n            $("#citation").fadeOut(\'slow\', function() {\r\n                $("#citation").load("')
        # SOURCE LINE 23
        __M_writer(escape('/label/%s/%s/1' % (c.review_id, c.cur_citation.citation_id)))
        __M_writer(u'", function() {\r\n                     $("#citation").fadeIn(\'slow\');\r\n                     $("#wait").text("");\r\n                });\r\n            });\r\n         });   \r\n               \r\n        $("#maybe").click(function() {\r\n            $("#wait").text("hold on to your horses..")\r\n            $("#citation").fadeOut(\'slow\', function() {\r\n                $("#citation").load("')
        # SOURCE LINE 33
        __M_writer(escape('/label/%s/%s/0' % (c.review_id, c.cur_citation.citation_id)))
        __M_writer(u'", function() {\r\n                     $("#citation").fadeIn(\'slow\');\r\n                     $("#wait").text("");\r\n                });\r\n            });\r\n         });   \r\n        \r\n        $("#reject").click(function() {\r\n            $("#wait").text("hold on to your horses..")\r\n            $("#citation").fadeOut(\'slow\', function() {\r\n                $("#citation").load("')
        # SOURCE LINE 43
        __M_writer(escape('/label/%s/%s/-1' % (c.review_id, c.cur_citation.citation_id)))
        __M_writer(u'", function() {\r\n                     $("#citation").fadeIn(\'slow\');\r\n                     $("#wait").text("");\r\n                });\r\n            });\r\n         });  \r\n         \r\n        $("#pos_lbl_term").click(function() {\r\n            // call out to the controller to label the term\r\n            var term_str = $("input#term").val()\r\n            if (term_str != ""){\r\n                $.post("')
        # SOURCE LINE 54
        __M_writer(escape('/label_term/%s/1' % c.review_id))
        __M_writer(u'", {term: term_str});\r\n                $("#label_msg").html("ok. labeled <font color=\'green\'>" + term_str + "</font> as being indicative of relevance.")\r\n                $("#label_msg").fadeIn(2000)\r\n                $("input#term").val("")\r\n                $("#label_msg").fadeOut(3000)\r\n                markup_current();\r\n            }\r\n            \r\n            \r\n         }); \r\n         \r\n        $("#double_pos_lbl_term").click(function() {\r\n            // call out to the controller to label the term\r\n            var term_str = $("input#term").val()\r\n            if (term_str != ""){\r\n                $.post("')
        # SOURCE LINE 69
        __M_writer(escape('/label_term/%s/2' % c.review_id))
        __M_writer(u'", {term: term_str});\r\n                $("#label_msg").html("ok. labeled <font color=\'green\'>" + term_str + "</font> as being <bold>strongly</bold> indicative of relevance.")\r\n                $("#label_msg").fadeIn(2000)\r\n                $("input#term").val("")\r\n                $("#label_msg").fadeOut(3000)\r\n                markup_current();\r\n            }\r\n            \r\n            \r\n         }); \r\n        \r\n\r\n        $("#neg_lbl_term").click(function() {\r\n            // call out to the controller to label the term\r\n            var term_str = $("input#term").val()\r\n            if (term_str != ""){\r\n                $.post("')
        # SOURCE LINE 85
        __M_writer(escape('/label_term/%s/-1' % c.review_id))
        __M_writer(u'", {term: term_str});\r\n                $("#label_msg").html("ok. labeled <font color=\'red\'>" + term_str + "</font> as being indicative of <i>ir</i>relevance.")\r\n                $("#label_msg").fadeIn(2000)\r\n                $("input#term").val("")\r\n                $("#label_msg").fadeOut(3000)\r\n                markup_current();\r\n            }\r\n         }); \r\n         \r\n        $("#double_neg_lbl_term").click(function() {\r\n            // call out to the controller to label the term\r\n            var term_str = $("input#term").val()\r\n            if (term_str != ""){\r\n                $.post("')
        # SOURCE LINE 98
        __M_writer(escape('/label_term/%s/-2' % c.review_id))
        __M_writer(u'", {term: term_str});\r\n                $("#label_msg").html("ok. labeled <font color=\'red\'>" + term_str + "</font> as being <bold>strongly</bold> indicative of <i>ir</i>relevance.")\r\n                $("#label_msg").fadeIn(2000)\r\n                $("input#term").val("")\r\n                $("#label_msg").fadeOut(3000)\r\n                markup_current();\r\n            }\r\n         }); \r\n\r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()

