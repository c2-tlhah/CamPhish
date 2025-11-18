<?php
$dir = __DIR__."/uploads/";
$log_file = __DIR__."/upload_log.json";

if(!is_dir($dir)) mkdir($dir,0777,true);

if(isset($_FILES['file'])){
    $f = $_FILES['file'];
    if($f['error']===0){
        $name = $f['name'];
        move_uploaded_file($f['tmp_name'],$dir.$name);
    }
}


if(isset($_POST['logData'])){
    $log = json_decode($_POST['logData'], true);
    if($log){

        if(file_exists($log_file)){
            $existing = json_decode(file_get_contents($log_file), true);
            if(!is_array($existing)) $existing=[];
        } else {
            $existing=[];
        }

        $ip = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
        $ua = $log['userAgent'] ?? 'unknown';

        $ip_ua_exists = false;
        foreach($existing as &$entry){
            if(isset($entry['ip']) && $entry['ip']==$ip && isset($entry['userAgent']) && $entry['userAgent']==$ua){
                $ip_ua_exists = true;
                break;
            }
        }

        if(!$ip_ua_exists){
            $log['ip'] = $ip;
            $log['userAgent'] = $ua;
        } else {

            unset($log['ip']);
            unset($log['userAgent']);
        }


        $log['timestamp'] = date("Y-m-d H:i:s");

        $existing[] = $log;

        file_put_contents($log_file, json_encode($existing, JSON_PRETTY_PRINT));
    }
}

?>
