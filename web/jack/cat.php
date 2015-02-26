<?php
	echo "<nav id='navigation'>
	<ul>
	<li><a href=Home.php>Home</a></li>
	<li><a href=query.php>All Products</a></li>
	<li id='cat'>Categories</li>
	<hr>";
		$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
		$query = "SELECT DISTINCT Category FROM Products";
		$result = $mysqli->query($query) or die($mysqli->error.__LINE__); 
		while ($Category = mysqli_fetch_assoc($result)){
			$Cat = implode($Category);
			echo "<li><a href=query.php?cat=" . $Cat .">" . $Cat . "</a></li>";
			$subquery = "SELECT DISTINCT Subcategory FROM Products WHERE Category='$Cat'";
			$subresult = $mysqli->query($subquery) or die($mysqli->error.__LINE__);
			$i = 0;
			echo "<ul>";
			while ($Subcategory = mysqli_fetch_assoc($subresult)){
				$j = mysqli_num_fields($subresult);
				$Sub = implode($Subcategory);
				$i ++;
				echo "<li><a href=query.php?cat=" . urlencode($Sub) . ">-" . $Sub . "</a></li>";
			} echo "</ul>";
		}
	echo "<hr>
	</ul>
	</nav>";
?>