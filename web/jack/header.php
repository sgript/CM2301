<?php
	echo '<a href="Home.php"><img src="Banner.png" id="Top" alt="Shopnet Home" width=300 Title="Shopnet Home" /></a>
		<form method="post" action="query.php" id="mainQuery">
				<input type="text" name="searchTerm" placeholder="Search for a product..."/>
				<select name="category">';
				$DB_NAME = 'c1327650';
				$DB_HOST = 'ephesus.cs.cf.ac.uk';
				$DB_USER = 'c1327650';
				$DB_PASS = 'berlin';
				$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
				$dquery = "SELECT DISTINCT Category FROM Products";
				$dresult = $mysqli->query($dquery) or die($mysqli->error.__LINE__); 
				echo "<option value='.' selected>All categories</option>";
				while ($dropdown = mysqli_fetch_assoc($dresult)){
			$drop = implode($dropdown);//fetch categories and subcategories, display them in dropdown
			echo "<option value=" . urlencode($drop) .">" . $drop . "</option>";
			$subq = "SELECT DISTINCT Subcategory FROM Products WHERE Category='$drop'";
			$subr = $mysqli->query($subq) or die($mysqli->error.__LINE__);
				while ($Subc = mysqli_fetch_assoc($subr)){
				$Subd = implode($Subc);
				echo "<option value=" . urlencode($Subd) . ">|--" . $Subd . "</option>";
			}
		}
	echo '</select>
	<input type="submit" name="submit" value="Go!"/>
	</form>';
?>