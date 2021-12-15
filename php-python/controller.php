<?php

$json_file_name = "data.json";

$command = "python piston.py " . $json_file_name;
$result = shell_exec($command);
echo '<pre>';
echo $result;
echo '<\pre>';
?>