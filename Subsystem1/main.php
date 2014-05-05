<?php
$hostname_localhost ="localhost";
$database_localhost ="es";
$username_localhost ="root";
$password_localhost ="asd";
$con = mysql_connect($hostname_localhost,$username_localhost,$password_localhost);
mysql_select_db($database_localhost, $con);

// Print Faults
function printFaults($name ,$l)
{
	echo $name.'<br/>';

	foreach($l as $fault)
	{
		echo $fault.'   ';
	}

	echo '<br/><br/>';
}

// Calculate distance b/w two Lat-Longs
function getDistanceFromLatLonInKm($lat1,$lon1,$lat2,$lon2) {
	$R = 6371; // Radius of the earth in km
	$dLat = deg2rad($lat2-$lat1);  // deg2rad below
	$dLon = deg2rad($lon2-$lon1); 
	$a = sin($dLat/2) * sin($dLat/2) +
		cos(deg2rad($lat1)) * cos(deg2rad($lat2)) * 
		sin($dLon/2) * sin($dLon/2)
		; 
	$c = 2 * atan2(sqrt($a), sqrt(1-$a)); 
	$d = $R * $c; // Distance in km
	return $d;
}

//Calculate top 5 faults
function getTopFive($allFaults)
{
	/*
	$fl=array();
	foreach($allFaults as $fault)
	{
		echo 'asd';
		$query_get_id="select * from fault_eq where fault_name=".$fault.";";
		$query_exec = mysql_query($query_get_id) or die(mysql_error());
		$res=mysql_fetch_assoc($query_exec);
		$id=$res["id"];
		array_push($fl,$id);
	}
	//$query_desc_eq="SELECT Fault_ID, Total_no_eq FROM fault_seismicity ORDER BY ~Total_no_eq;";
	//$query_exec = mysql_query($query_get_id) or die(mysql_error());
	
	$main_dict=array();
	 */
	$fl=$allFaults;
	foreach($fl as $fname)
	{
		$query_getquakes="select * from faults where fault_name='".$fname."';";
		$query_exec = mysql_query($query_getquakes) or die(mysql_error());
		$res=mysql_fetch_assoc($query_exec);
		$total_quakes=$res["eq_number"];
		$main_dict[$fname]=$total_quakes;
		
	}
	arsort($main_dict);
	print_r($main_dict);

}

$query_search="select * from faultlatlongs";

//Faults inside GUJARAT radius
$query_exec = mysql_query($query_search) or die(mysql_error());
$rows=mysql_num_rows($query_exec);
$l=array();
while($res=mysql_fetch_assoc($query_exec))
{
	if(getDistanceFromLatLonInKm($res["fault_lat"],$res["fault_long"],23.2167,72.6833) < 343)
	{
		array_push($l,$res["faultname"]);
		$l=array_unique($l);
	}
}
$guju=$l;
printFaults("Gujarat", $guju);
getTopFive($guju);

//Faults inside NORTH EAST radius
$query_exec = mysql_query($query_search) or die(mysql_error());
$l=array();
while($res=mysql_fetch_assoc($query_exec))
{
	if(getDistanceFromLatLonInKm($res["fault_lat"],$res["fault_long"],26.1400,91.7700) < 485)
	{
		array_push($l,$res["faultname"]);
		$l=array_unique($l);
	}
}
$ne=$l;
printFaults("North East", $ne);
getTopFive($ne);


//Faults inside HIMACHAL radius
$query_exec = mysql_query($query_search) or die(mysql_error());
$l=array();
while($res=mysql_fetch_assoc($query_exec))
{
	if(getDistanceFromLatLonInKm($res["fault_lat"],$res["fault_long"],33.0200,77.2100) < 187)
	{
		array_push($l,$res["faultname"]);
		$l=array_unique($l);
	}
}
$himachal=$l;
printFaults("Himachal", $himachal);
getTopFive($himachal);



/*for($i=0;$i<count($l);$i++)
{
    echo $l[$i];
}/
/*$solved[$level]=$rows;
}
for($level=1;$level<=5;$level++)
{
echo "<div id='s".$level."'>".$solved[$level]."</div>"; //do it hidden while using jquery 
echo "<br/>";
}*/
?>
