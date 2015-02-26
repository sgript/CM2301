<?php	
	$qtest = mysqli_num_rows($qresult);
	if ($qtest > 0){
	echo "<form method='get' action='query.php' id='sortBy' name=sortform>
		<select name='sort' onChange='javascript:document.sortform.submit();'>
		<option value='' selected>Sort by...</option>
		<option value='Manufacturer ASC'>Manufacturer A-Z</option>
		<option value='Manufacturer DESC'>Manufacturer Z-A</option>
		<option value='Name ASC'>Name A-Z</option>
		<option value='Name ASC'>Name Z-A</option>
		<option value='Price ASC'>Price Low-High</option>
		<option value='Price DESC'>Price High-Low</option>
		</select>";
		if ((isset($_GET['cat'])) OR ((isset($_POST['searchTerm'])) AND (isset($_POST['category'])))){
		echo "<input type='hidden' name='srch' value='" . $search . "'/>
		<input type='hidden' name='cat' value='" . $pcat . "'/>";
		} else {
		}
		echo "
		<noscript>
		<input type='submit' name='submit' value='Filter'/>
		</noscript>
		</form>
		<table>
		<thead>
		<th class='head'></th><th class='head'>Product</th><th class='head'>Price</th>
		</thead>";
	} else {
			echo "Sorry, no results. Try another search term?";
	}
?>