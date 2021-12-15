<?php

$curl = curl_init();
$token = "57d1f2a8-4394-4458-8093-abed75873037";
curl_setopt_array($curl, [
	CURLOPT_URL => "https://judge0-ce.p.rapidapi.com/submissions/".$token."?base64_encoded=true&fields=*",
	CURLOPT_RETURNTRANSFER => true,
	CURLOPT_FOLLOWLOCATION => true,
	CURLOPT_ENCODING => "",
	CURLOPT_MAXREDIRS => 10,
	CURLOPT_TIMEOUT => 30,
	CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
	CURLOPT_CUSTOMREQUEST => "GET",
	CURLOPT_HTTPHEADER => [
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