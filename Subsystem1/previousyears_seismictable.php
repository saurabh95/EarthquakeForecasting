<?php
$hostname_localhost ="localhost";
$database_localhost ="es";
$username_localhost ="root";
$password_localhost ="saurabh";
$fault=array('917','248','214','240','238');
$range=array("3 AND 3.5","3.5 AND 4","4 AND 4.5","4.5 AND 5","5 AND 5.5","5.5 AND 6","6 AND 6.5","6.5 AND 7");
$con = mysql_connect($hostname_localhost,$username_localhost,$password_localhost);
mysql_select_db($database_localhost, $con);
echo"<h1>Haridwar</h1>
		<table class='zebra'>
			<thead>
				<tr>
					<th>Magnitude</th>
					<th>Fault ".$fault[0]."</th>
					<th>Fault ".$fault[1]."</th>
					<th>Fault ".$fault[2]."</th>
					<th>Fault ".$fault[3]."</th>
					<th>Fault ".$fault[4]."</th>
				</tr>
			</thead>
			<tbody>\n";

foreach($range as $r)
{
$s=$r;
$s=str_replace("AND","-",$s);
echo "<tr>\n<td>".$s."</td>\n";
$query_search="SELECT count(*) as cont FROM  earthquake WHERE  fault_name='".$fault[0]."' AND (m BETWEEN ".$r.")";
$query_exec = mysql_query($query_search) or die(mysql_error());
while($res = mysql_fetch_assoc($query_exec)) {
	echo "<td>".$res['cont']."</td>";
	echo "\n";
}
$query_search="SELECT count(*) as cont FROM  earthquake WHERE  fault_name='".$fault[1]."' AND (m BETWEEN ".$r.")";
$query_exec = mysql_query($query_search) or die(mysql_error());
while($res = mysql_fetch_assoc($query_exec)) {
	echo "<td>".$res['cont']."</td>";
	echo "\n";
}
$query_search="SELECT count(*) as cont FROM  earthquake WHERE  fault_name='".$fault[2]."' AND (m BETWEEN ".$r.")";
$query_exec = mysql_query($query_search) or die(mysql_error());
while($res = mysql_fetch_assoc($query_exec)) {
	echo "<td>".$res['cont']."</td>";
	echo "\n";
}
$query_search="SELECT count(*) as cont FROM  earthquake WHERE  fault_name='".$fault[3]."' AND (m BETWEEN ".$r.")";
$query_exec = mysql_query($query_search) or die(mysql_error());
while($res = mysql_fetch_assoc($query_exec)) {
	echo "<td>".$res['cont']."</td>";
	echo "\n";
}
$query_search="SELECT count(*) as cont FROM  earthquake WHERE  fault_name='".$fault[4]."' AND (m BETWEEN ".$r.")";
$query_exec = mysql_query($query_search) or die(mysql_error());
while($res = mysql_fetch_assoc($query_exec)) {
	echo "<td>".$res['cont']."</td>";
	echo "\n";
echo "</tr>\n\n";
}

}
echo "</tbody>\n</table>\n\n";





?>
