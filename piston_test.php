<?php

$url = "https://emkc.org/api/v1/piston/execute";

$curl = curl_init();

$src = "print('hello world!')";

$data = [
    "language : python3",
    "source :" .$src,
    // "stdin :".$stdin
];

// $data->language = "python3";
// $data->source = $src;

$dataInJSON = json_encode($data);

// curl_setopt($curl, CURLOPT_POST, $dataInJSON);

curl_setopt_array($curl, 
[
	CURLOPT_URL => $url,
	CURLOPT_RETURNTRANSFER => true,
	CURLOPT_FOLLOWLOCATION => true,
	CURLOPT_ENCODING => "",
	CURLOPT_MAXREDIRS => 10,
	CURLOPT_TIMEOUT => 30,
	CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
	CURLOPT_CUSTOMREQUEST => "POST",
	CURLOPT_POSTFIELDS => $dataInJSON
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err)
{
	echo "cURL Error #:" . $err;
}
else 
{
	echo $response;
}

?>