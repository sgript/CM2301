<?php
	// Connects to database with login details, shows you if connection has failed through printf
	$DB_HOST = 'ephesus.cs.cf.ac.uk';
	$DB_NAME = 'c1312433';
	$DB_USER = 'c1312433';
	$DB_PASS = 'berlin';
	$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
		if (mysqli_connect_errno()) {
			printf("Connect failed: %s\n", mysqli_connect_error());
			exit();
		}
?>