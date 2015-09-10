<?php
//Get the user's comment.
//01/28/2015 Rpierce
$comment = $_POST["comment"];
//Append it to the comments file.
$f = fopen("comments.txt", "w");
fwrite($f, $comment);
fclose($f);
//Jump back to Renata's page.
header("location:google.com");
?>
