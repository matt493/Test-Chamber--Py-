<?php

$curl = curl_init();

$src = "54321 ";
echo $src;
$stdin = "";
$lang_id = 71;

curl_setopt_array($curl, [
	CURLOPT_URL => "https://judge0-ce.p.rapidapi.com/submissions?base64_encoded=true&wait=true&fields=*",
	CURLOPT_RETURNTRANSFER => true,
	CURLOPT_FOLLOWLOCATION => true,
	CURLOPT_ENCODING => "",
	CURLOPT_MAXREDIRS => 10,
	CURLOPT_TIMEOUT => 30,
	CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
	CURLOPT_CUSTOMREQUEST => "POST",
	CURLOPT_POSTFIELDS => "{\r\n    \"language_id\": ".$lang_id.",\r\n    \"source_code\": \"".$src."\",\r\n    \"stdin\": \"".$stdin."\"\r\n}",
	CURLOPT_HTTPHEADER => [
		"content-type: application/json",
		"x-rapidapi-host: judge0-ce.p.rapidapi.com",
		"x-rapidapi-key: 4ceb9ab2b1msh481656cca070ccbp145af6jsnf68fc092f615"
	],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
	echo "cURL Error #:" . $err;
} else {
	echo $response;
}