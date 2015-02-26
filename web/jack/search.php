<!DOCTYPE html > 
<html lang=”en”>
	<head>
		<title>Name</title>
	</head>
	<body>
		<?php
			$searchTerm = $_POST['searchTerm'];
			$searchField = $_POST['searchField'];

			// CONNECT TO THE DATABASE
			$DB_NAME = 'c1327650';
			$DB_HOST = 'ephesus.cs.cf.ac.uk';
			$DB_USER = 'c1327650';
			$DB_PASS = 'berlin';
			$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
			if (mysqli_connect_errno()) {
				printf("Connect failed: %s\n", mysqli_connect_error());
				exit();
			}

			// Query to output all students born in 1987
			$query = "SELECT * FROM Products WHERE * LIKE ' $searchTerm '";
			$result = $mysqli->query($query) or die($mysqli->error.__LINE__);

			// GOING THROUGH THE DATA
			if($result->num_rows > 0) {
				while($row = $result->fetch_assoc()) {
					echo stripslashes($row['FirstName']) . " " . $row['LastName'];	
					echo "<br>";
				}
			} else {
				echo 'NO RESULT FOUND';	
			}

			// CLOSE CONNECTION
			mysqli_close($mysqli);
		?>
	</body>
</html>
