<?php
  error_reporting (E_ALL ^ E_NOTICE);
  
  $con = mysqli_connect("ephesus.cs.cf.ac.uk","c1312433","berlin","c1312433");
  if (mysqli_connect_errno()) {
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
  }
  else
    echo "<center><img src='faceten.gif' alt='faceten'></center>";
  session_start(); 
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>Manage user groups</title>
 
    <link type="text/css" rel="stylesheet" href="css/bootstrap.css"/>

    <link href="manageusergroups.css" rel="stylesheet">

    <script src="error.js"></script>

  </head>

  <body>

     

    <div class="container">

    <?php 
    session_start();
    if (isset($_SESSION['username'])) {
       session_destroy();
       echo "You are logged out successfully!";
    } 
       echo "<a href='login.php' class = link2>Log Out</a>";
     ?>
      <div class="masthead">
        <nav>
          <ul class="nav nav-justified">
            <li><a href="#">Manage Users</a></li>
            <li class="active"><a href="livefeed.html">Live Feed</a></li>
            <li><a href="manageusergroups.html">Manage User Groups</a></li>
          </ul>
        </nav>

      </div>
        <table class="table-striped">
          <tr>
            <th scope="col">User Group Name</th>
            <th scope="col">Available/Permitted Rooms</th> 
            <th scope="col">Options</th> 
          </tr>
          <tr>
            <td>A</td>
            <td>T2.09, T2.07</td>
            <td>Remove/edit</td>
          </tr>
          <tr>
            <td>B</td>
            <td>C2.07, C2.04</td>
            <td>Remove/edit</td>
          </tr> 
           <tr>
            <td>C</td>
            <td>S1.32, S2.15</td>
            <td>Remove/edit</td>
          </tr> 
        </table>
    </div>   
  </body>
</html>