<?php
print(1);
    $formName =  'http://192.168.15.200:5000/getform.php?cache_enabled=0&Form=Tutorial%2Fmain&cache=c8db972d36331a3f650807a99a2c38b2a';

//initial request with login data

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,$formName );
curl_setopt($ch, CURLOPT_USERAGENT,'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/32.0.1700.107 Chrome/32.0.1700.107 Safari/537.36');
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_COOKIESESSION, true);
curl_setopt($ch, CURLOPT_COOKIEFILE, 'tmp');  //could be empty, but cause problems on some hosts
//curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookie-name');  //could be empty, but cause problems on some hosts
//curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
//curl_setopt($ch, CURLOPT_POSTFIELDS, "username=XXXXX&password=XXXXX");
$answer = curl_exec($ch);
if (curl_error($ch)) {
    echo curl_error($ch);
}else{
	print($answer);
}

print("============");

curl_setopt($ch, CURLOPT_URL, $formName );
curl_setopt($ch, CURLOPT_POST, false);
curl_setopt($ch, CURLOPT_POSTFIELDS, "");
$answer = curl_exec($ch);
if (curl_error($ch)) {
    echo curl_error($ch);
}else{
	print($answer);
}
			 
print("============");

curl_setopt($ch, CURLOPT_URL, $formName );
curl_setopt($ch, CURLOPT_POST, false);
curl_setopt($ch, CURLOPT_POSTFIELDS, "");
$answer = curl_exec($ch);
if (curl_error($ch)) {
    echo curl_error($ch);
}else{
	print($answer);
}
			 
print("============");

curl_setopt($ch, CURLOPT_URL, $formName );
curl_setopt($ch, CURLOPT_POST, false);
curl_setopt($ch, CURLOPT_POSTFIELDS, "");
$answer = curl_exec($ch);
if (curl_error($ch)) {
    echo curl_error($ch);
}else{
	print($answer);
}
			 
print("============");

curl_setopt($ch, CURLOPT_URL, $formName );
curl_setopt($ch, CURLOPT_POST, false);
curl_setopt($ch, CURLOPT_POSTFIELDS, "");
$answer = curl_exec($ch);
if (curl_error($ch)) {
    echo curl_error($ch);
}else{
	print($answer);
}
			 
		 
print("============");

curl_setopt($ch, CURLOPT_URL, $formName );
curl_setopt($ch, CURLOPT_POST, false);
curl_setopt($ch, CURLOPT_POSTFIELDS, "");
$answer = curl_exec($ch);
if (curl_error($ch)) {
    echo curl_error($ch);
}else{
	print($answer);
}
			 
		 
print("============");

curl_setopt($ch, CURLOPT_URL, $formName );
curl_setopt($ch, CURLOPT_POST, false);
curl_setopt($ch, CURLOPT_POSTFIELDS, "");
$answer = curl_exec($ch);
if (curl_error($ch)) {
    echo curl_error($ch);
}else{
	print($answer);
}
			 
		 
print("============");

curl_setopt($ch, CURLOPT_URL, $formName );
curl_setopt($ch, CURLOPT_POST, false);
curl_setopt($ch, CURLOPT_POSTFIELDS, "");
$answer = curl_exec($ch);
if (curl_error($ch)) {
    echo curl_error($ch);
}else{
	print($answer);
}
			 
		 
print("============");

curl_setopt($ch, CURLOPT_URL, $formName );
curl_setopt($ch, CURLOPT_POST, false);
curl_setopt($ch, CURLOPT_POSTFIELDS, "");
$answer = curl_exec($ch);
if (curl_error($ch)) {
    echo curl_error($ch);
}else{
	print($answer);
}
			 
		 
print("============");

curl_setopt($ch, CURLOPT_URL, $formName );
curl_setopt($ch, CURLOPT_POST, false);
curl_setopt($ch, CURLOPT_POSTFIELDS, "");
$answer = curl_exec($ch);
if (curl_error($ch)) {
    echo curl_error($ch);
}else{
	print($answer);
}
			 



  print("ok");
 curl_close ($curl);//закрытие сеанса
  
  
  
/*  

openD3Form('test2');

//initial request with login data
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'http://www.example.com/login.php');
curl_setopt($ch, CURLOPT_USERAGENT,'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/32.0.1700.107 Chrome/32.0.1700.107 Safari/537.36');
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, "username=XXXXX&password=XXXXX");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_COOKIESESSION, true);
curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookie-name');  //could be empty, but cause problems on some hosts
curl_setopt($ch, CURLOPT_COOKIEFILE, '/var/www/ip4.x/file/tmp');  //could be empty, but cause problems on some hosts
$answer = curl_exec($ch);
if (curl_error($ch)) {
    echo curl_error($ch);
}

//another request preserving the session
curl_setopt($ch, CURLOPT_URL, 'http://www.example.com/profile');
curl_setopt($ch, CURLOPT_POST, false);
curl_setopt($ch, CURLOPT_POSTFIELDS, "");
$answer = curl_exec($ch);
if (curl_error($ch)) {
    echo curl_error($ch);
}
*/

?>