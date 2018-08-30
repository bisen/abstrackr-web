<script type="text/javascript">
	$(document).ready(function() {
		$("#export_btn").unbind();

	    $("#export_btn").click(function()
	    {

	       // now add all selected tags to the study
	       var fields = $.map($('.ui-selected, this'), function(element, i) {
	         return $(element).text();
	       });
				 var export_type = $('#export_type').val()
		   	 $("#export").load('/exporting.html', function(){
	       		$("#export").load("${'/review/export_labels/%s' % c.review_id}", {fields: fields, export_type: export_type});
				 });


	    });
	 });
</script>

<h1>export labels</h1>

<span> select the export type: </span>
<select id="export_type">
  <option value="csv" checked> CSV </option>
  <option value="xml"> XML</option>
  <option value="ris-citations"> RIS (citations)</option>
  <option value="ris-labels"> RIS (labels)</option>
</select>
<br/>
<br/>


select the fields you'd like to export:<br/>

<center>
<ul id="selectable" class="ui-selectable">
% for field in ["(internal) id", "(source) id", "pubmed id", "keywords", "abstract", "title", "journal", "authors", "tags", "notes"]:
 	<li class="ui-selected">${field}</li>
% endfor

% for field in []:
	<li class="ui-selectee">${field}</li>
% endfor
</ul>

</center>
<br/>
<div class="actions">
<input id="export_btn" type="button" value="export" />
</div>
