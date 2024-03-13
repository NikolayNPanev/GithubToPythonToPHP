<?php
$command = escapeshellcmd("GetData.py");
$output = shell_exec($command);
echo $output;
?>