# ScrapyWeldArc
Retrieving information on welding arcs via robot


#this a page example for make web scraping
#the objective is retrieving Weld_Schedule_Data information this page contains 2 tables with different columns

#There are 2 spiders file (lincolnSpider and froniusSpider) 
#activate virtual enviroment 
#run the command "scrapy crawl lincolnSpider" or "scrapy crawl froniusSpider" to execute spider
#


<html>
<head>
<meta http-equiv="Cache-Control" content="no-cache">
<meta http-equiv="Cache-Control" content="no-store">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<title> RESPONSE.HTM </title>
</head>
<BODY bgcolor= #FFF9e3>

<table width="100%" border="1">
  <tr>
  <td>
  <table width="100%" bgcolor=#FFFFFF>
  <tr>
  <td align=left valign=middle><img src="/frs/logo.png"></td>
  <td align=center valign=middle><strong><font color=#e60000 size=6>
Arc Data</font><br>
        <font color=black size=3>
Hostname: 170RW02<br>
Robot No: F270030    <br>
        </font></strong></td>
  <td align=right valign=middle><img src="/frs/logo.png"></td>
  </tr>
  </table>
  </td>
  </tr>
</table>
<BR>
 <div align="center">
<a href="#Weld_System_Setup">Weld System Setup</a><BR>
<BR>
<a href="#Weld_Procedure_Data">Weld Procedure Data
</a><BR>
<BR>
<a href="#Weave_Schedule_Data">Weave Schedule Data</a><BR>
</div>
<BR><BR><BR><BR><BR><BR>
<a name="Weld_System_Setup"></a><H2 align="center">
Weld System Setup</H2>
<table width="100%" border="1">
<tr align="left">
<td>
Number of weld equipment</td>
<td>
  1
</td>
</tr>
<tr align="left">
<td>
Multi-process</td>
<td>
 TRUE
</td>
<tr align="left">
<td>
Weld procedures
</td>
<td>
 TRUE
</td>
</tr>
</table>
<BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR>
<a name="Weld_Procedure_Data"></a><H2 align="center">
Weld Procedure Data</H2>
<table width="100%" border="1">
<tr align="center">
<td>
<b>
WP</b>
</td>
<td>
<b>
Sch</b>
</td>
<td>
<b>
Runin</b>
</td>
<td>
<b>
Bback</b>
</td>
<td>
<b>
Wstick</b>
</td>
<td>
<b>
Ramp</b>
</td>
<td>
<b>
Mode</b>
</td>
<td>
<b>
Description</b>
</td>
</tr>
<tr align="right" bgcolor="#99FF99">
<td>
            1</td>
<td>
<a href="#AWE1WP01">           32</a></td>
<td>
  TRUE       </td>
<td>
  TRUE       </td>
<td>
  TRUE       </td>
<td>
  FALSE      </td>
<td>
          274</td>
<td>
 Rapid X                 </td>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</table>
<BR>
<BR>
<a name="AWE1WP01"></a><H2 align="center">
</H2>
<a name="Weld_Schedule_Data"></a><H2 align="center">
Weld Procedure  1
Weld Schedule Data</H2>
<table width="100%" border="1">
<tr align="center">
<td>
<b>
Num</b>
</td>
<td>
<b>
WFS</b>
</td>
<td>
<b>
Trim</b>
</td>
<td>
<b>
UltimArc</b>
</td>
<td>
<b>
Weld Speed</b>
</td>
<td>
<b>
Time</b>
</td>
<td>
<b>
Comment</b>
</td>
</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
   1</td>
<td>
 440.000 IPM</td>
<td>
  .900 </td>
<td>
 -3.000 </td>
<td>
 48.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">58_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
   2</td>
<td>
 440.000 IPM</td>
<td>
  .900 </td>
<td>
 -3.000 </td>
<td>
 48.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">62_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
   3</td>
<td>
 330.000 IPM</td>
<td>
  .900 </td>
<td>
 -3.000 </td>
<td>
 27.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">236_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
   4</td>
<td>
 330.000 IPM</td>
<td>
  .900 </td>
<td>
 -3.000 </td>
<td>
 33.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">24_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
   5</td>
<td>
 330.000 IPM</td>
<td>
  .900 </td>
<td>
 -3.000 </td>
<td>
 27.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">232_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
   6</td>
<td>
 460.000 IPM</td>
<td>
  .900 </td>
<td>
 -3.000 </td>
<td>
 46.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">18_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
   7</td>
<td>
 460.000 IPM</td>
<td>
  .900 </td>
<td>
 -3.000 </td>
<td>
 46.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">72_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
   8</td>
<td>
 460.000 IPM</td>
<td>
  .900 </td>
<td>
 -3.000 </td>
<td>
 44.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">74_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
   9</td>
<td>
 473.000 IPM</td>
<td>
  .900 </td>
<td>
 -3.000 </td>
<td>
 44.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">76_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  10</td>
<td>
 315.000 IPM</td>
<td>
  .930 </td>
<td>
 -3.000 </td>
<td>
 30.000 IPM</td>
<td>
  .120 sec</td>
<td>
 <div align="left">98_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  11</td>
<td>
 315.000 IPM</td>
<td>
  .930 </td>
<td>
 -3.000 </td>
<td>
 30.000 IPM</td>
<td>
  .120 sec</td>
<td>
 <div align="left">100_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  12</td>
<td>
 0.000 IPM</td>
<td>
 0.000 </td>
<td>
 0.000 </td>
<td>
 0.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">.</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  13</td>
<td>
 0.000 IPM</td>
<td>
 0.000 </td>
<td>
 0.000 </td>
<td>
 0.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">.</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  14</td>
<td>
 0.000 IPM</td>
<td>
 0.000 </td>
<td>
 0.000 </td>
<td>
 50.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">.</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  15</td>
<td>
 0.000 IPM</td>
<td>
 0.000 </td>
<td>
 0.000 </td>
<td>
 0.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left"></div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  16</td>
<td>
 410.000 IPM</td>
<td>
  .860 </td>
<td>
 -3.000 </td>
<td>
 41.000 IPM</td>
<td>
  .500 sec</td>
<td>
 <div align="left">233_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  17</td>
<td>
 270.000 IPM</td>
<td>
  .910 </td>
<td>
 0.000 </td>
<td>
 30.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">131_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  18</td>
<td>
 440.000 IPM</td>
<td>
  .900 </td>
<td>
 -3.000 </td>
<td>
 43.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">55_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  19</td>
<td>
 390.000 IPM</td>
<td>
  .860 </td>
<td>
 -3.000 </td>
<td>
 49.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">43_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  20</td>
<td>
 440.000 IPM</td>
<td>
  .860 </td>
<td>
 -3.000 </td>
<td>
 48.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">21_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  21</td>
<td>
 440.000 IPM</td>
<td>
  .880 </td>
<td>
 -3.000 </td>
<td>
 48.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">57_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  22</td>
<td>
 440.000 IPM</td>
<td>
  .880 </td>
<td>
 -3.000 </td>
<td>
 48.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">61_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  23</td>
<td>
 330.000 IPM</td>
<td>
  .820 </td>
<td>
 -3.000 </td>
<td>
 27.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">69_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  24</td>
<td>
 330.000 IPM</td>
<td>
  .820 </td>
<td>
 -3.000 </td>
<td>
 27.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">77_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  25</td>
<td>
 440.000 IPM</td>
<td>
  .860 </td>
<td>
 -3.000 </td>
<td>
 46.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">103_1</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  26</td>
<td>
 0.000 IPM</td>
<td>
 0.000 </td>
<td>
 0.000 </td>
<td>
 0.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">.</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  27</td>
<td>
 0.000 IPM</td>
<td>
 0.000 </td>
<td>
 0.000 </td>
<td>
 0.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">.</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  28</td>
<td>
 0.000 IPM</td>
<td>
 0.000 </td>
<td>
 0.000 </td>
<td>
 0.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">.</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  29</td>
<td>
 0.000 IPM</td>
<td>
 0.000 </td>
<td>
 0.000 </td>
<td>
 0.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">.</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  30</td>
<td>
 260.000 IPM</td>
<td>
  .800 </td>
<td>
 -5.000 </td>
<td>
 33.000 IPM</td>
<td>
  .500 sec</td>
<td>
 <div align="left">TAG</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  31</td>
<td>
 0.000 IPM</td>
<td>
 0.000 </td>
<td>
 0.000 </td>
<td>
 0.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">.</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  32</td>
<td>
 0.000 IPM</td>
<td>
 0.000 </td>
<td>
 0.000 </td>
<td>
 0.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">.</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  33</td>
<td>
 280.000 IPM</td>
<td>
  .900 </td>
<td>
 0.000 </td>
<td>
 </td>
<td>
 0.000 sec</td>
<td>
 <div align="left">Runin</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  34</td>
<td>
 250.000 IPM</td>
<td>
  .900 </td>
<td>
 0.000 </td>
<td>
 </td>
<td>
  .080 sec</td>
<td>
 <div align="left">Burnback</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  35</td>
<td>
 300.000 IPM</td>
<td>
 1.000 </td>
<td>
 0.000 </td>
<td>
 </td>
<td>
  .100 sec</td>
<td>
 <div align="left">Wirestick</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  36</td>
<td>
 5.800 IPM</td>
<td>
  .010 </td>
<td>
  .200 </td>
<td>
 1.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">OnTheFly</div>
</td>

</tr>
</table>
<BR>
<BR>
<BR><BR><BR><BR><BR><BR><BR><BR>
<a name="Weave_Schedule_Data"></a><H2 align="center">
Weave Schedule Data</H2>
<table width="100%" border="1">
<tr align="center">
<td>
<b>
Num</b>
</td>
<td>
<b>
FREQ(Hz)</b>
</td>
<td>
<b>
AMP(mm)</b>
</td>
<td>
<b>
R_DW(sec)</b>
</td>
<td>
<b>
L_DW(sec)</b>
</td>
</tr>
<tr align="right" bgcolor="#99FF99">
<td>
   1</td>
<td>
 6.000
</td>
<td>
  .500
</td>
<td>
  .800
</td>
<td>
  .800
</td>
</tr>
<tr align="right">
<td>
   2</td>
<td>
 10.000
</td>
<td>
 2.500
</td>
<td>
  .100
</td>
<td>
  .100
</td>
</tr>
<tr align="right" bgcolor="#99FF99">
<td>
   3</td>
<td>
 6.000
</td>
<td>
 1.000
</td>
<td>
  .800
</td>
<td>
  .800
</td>
</tr>
<tr align="right">
<td>
   4</td>
<td>
 1.000
</td>
<td>
 4.000
</td>
<td>
  .100
</td>
<td>
  .100
</td>
</tr>
<tr align="right" bgcolor="#99FF99">
<td>
   5</td>
<td>
 1.000
</td>
<td>
 4.000
</td>
<td>
  .100
</td>
<td>
  .100
</td>
</tr>
<tr align="right">
<td>
   6</td>
<td>
 1.000
</td>
<td>
 4.000
</td>
<td>
  .100
</td>
<td>
  .100
</td>
</tr>
<tr align="right" bgcolor="#99FF99">
<td>
   7</td>
<td>
 1.000
</td>
<td>
 4.000
</td>
<td>
  .100
</td>
<td>
  .100
</td>
</tr>
<tr align="right">
<td>
   8</td>
<td>
 1.000
</td>
<td>
 4.000
</td>
<td>
  .100
</td>
<td>
  .100
</td>
</tr>
<tr align="right" bgcolor="#99FF99">
<td>
   9</td>
<td>
 1.000
</td>
<td>
 4.000
</td>
<td>
  .100
</td>
<td>
  .100
</td>
</tr>
<tr align="right">
<td>
  10</td>
<td>
 1.000
</td>
<td>
 4.000
</td>
<td>
  .100
</td>
<td>
  .100
</td>
</tr>
</table>
<BR>
<BR>
<pre>
<!--#include file=frs:default.tlr -->

############################################################################################
############################################################################################
############################################################################################

<html>
<HEAD>
<meta http-equiv="Cache-Control" content="no-cache">
<meta http-equiv="Cache-Control" content="no-cache">
<meta http-equiv="Cache-Control" content="no-store">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<title> RESPONSE.HTM </title>
</head>
<BODY bgcolor= #FFF9e3>

<table width="100%" border="1">
  <tr>
  <td>
  <table width="100%" bgcolor=#FFFFFF>
  <tr>
  <td align=left valign=middle><img src="/frs/logo.png"></td>
  <td align=center valign=middle><strong><font color=#e60000 size=6>
Arc Data</font><br>
        <font color=black size=3>
Hostname: R2ST80<br>
Robot No: F199492    <br>
        </font></strong></td>
  <td align=right valign=middle><img src="/frs/logo.png"></td>
  </tr>
  </table>
  </td>
  </tr>
</table>
<BR>
 <div align="center">
<a href="#Weld_System_Setup">Weld System Setup</a><BR>
<BR>
<a href="#Weld_Procedure_Data">Weld Procedure Data
</a><BR>
<BR>
<a href="#Weave_Schedule_Data">Weave Schedule Data</a><BR>
</div>
<BR><BR><BR><BR><BR><BR>
<a name="Weld_System_Setup"></a><H2 align="center">
Weld System Setup</H2>
<table width="100%" border="1">
<tr align="left">
<td>
Number of weld equipment</td>
<td>
  1
</td>
</tr>
<tr align="left">
<td>
Multi-process</td>
<td>
 TRUE
</td>
<tr align="left">
<td>
Weld procedures
</td>
<td>
 TRUE
</td>
</tr>
</table>
<BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR>
<a name="Weld_Procedure_Data"></a><H2 align="center">
Weld Procedure Data</H2>
<table width="100%" border="1">
<tr align="center">
<td>
<b>
WP</b>
</td>
<td>
<b>
Sch</b>
</td>
<td>
<b>
Runin</b>
</td>
<td>
<b>
Bback</b>
</td>
<td>
<b>
Wstick</b>
</td>
<td>
<b>
Ramp</b>
</td>
<td>
<b>
Mode</b>
</td>
<td>
<b>
Description</b>
</td>
</tr>
<tr align="right" bgcolor="#99FF99">
<td>
            1</td>
<td>
<a href="#AWE1WP01">           16</a></td>
<td>
  FALSE      </td>
<td>
  FALSE      </td>
<td>
  FALSE      </td>
<td>
  FALSE      </td>
<td>
            3</td>
<td>
 Job Mode                </td>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</tr>
</table>
<BR>
<BR>
<a name="AWE1WP01"></a><H2 align="center">
</H2>
<a name="Weld_Schedule_Data"></a><H2 align="center">
Weld Procedure  1
Weld Schedule Data</H2>
<table width="100%" border="1">
<tr align="center">
<td>
<b>
Num</b>
</td>
<td>
<b>
Job Number</b>
</td>
<td>
<b>
Weld Speed</b>
</td>
<td>
<b>
Time</b>
</td>
<td>
<b>
Comment</b>
</td>
</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
   1</td>
<td>
 1.000 </td>
<td>
 20.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">Wd.27-80</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
   2</td>
<td>
 2.000 </td>
<td>
 20.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">Wd.25-80</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
   3</td>
<td>
 3.000 </td>
<td>
 40.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">Wd119-80</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
   4</td>
<td>
 4.000 </td>
<td>
 20.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">Wd.61-80</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
   5</td>
<td>
 5.000 </td>
<td>
 24.000 IPM</td>
<td>
  .030 sec</td>
<td>
 <div align="left">Wd.85-80</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
   6</td>
<td>
 6.000 </td>
<td>
 40.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">Wd.87-80</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
   7</td>
<td>
 7.000 </td>
<td>
 27.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">Wd_95-80</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
   8</td>
<td>
 8.000 </td>
<td>
 38.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">Wd.15-80</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
   9</td>
<td>
 9.000 </td>
<td>
 40.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left"></div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  10</td>
<td>
 10.000 </td>
<td>
 40.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">Wd.125-81</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  11</td>
<td>
 11.000 </td>
<td>
 45.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">Wd.47-81</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  12</td>
<td>
 12.000 </td>
<td>
 40.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left"></div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  13</td>
<td>
 13.000 </td>
<td>
 36.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left"></div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  14</td>
<td>
 14.000 </td>
<td>
 36.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left"></div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  15</td>
<td>
 15.000 </td>
<td>
 37.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left"></div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  16</td>
<td>
 0.000 </td>
<td>
 50.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">Schedule</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  17</td>
<td>
 20.000 </td>
<td>
 </td>
<td>
 0.000 sec</td>
<td>
 <div align="left">Runin</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  18</td>
<td>
 20.000 </td>
<td>
 </td>
<td>
  .100 sec</td>
<td>
 <div align="left">Burnback</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFF00">
<td>
  19</td>
<td>
 20.000 </td>
<td>
 </td>
<td>
  .100 sec</td>
<td>
 <div align="left">Wirestick</div>
</td>

</tr>
<tr align="right" bgcolor="#FFFFFF">
<td>
  20</td>
<td>
  .100 </td>
<td>
 1.000 IPM</td>
<td>
 0.000 sec</td>
<td>
 <div align="left">OnTheFly</div>
</td>

</tr>
</table>
<BR>
<BR>
<BR><BR><BR><BR><BR><BR><BR><BR>
<a name="Weave_Schedule_Data"></a><H2 align="center">
Weave Schedule Data</H2>
<table width="100%" border="1">
<tr align="center">
<td>
<b>
Num</b>
</td>
<td>
<b>
FREQ(Hz)</b>
</td>
<td>
<b>
AMP(mm)</b>
</td>
<td>
<b>
R_DW(sec)</b>
</td>
<td>
<b>
L_DW(sec)</b>
</td>
</tr>
<tr align="right" bgcolor="#99FF99">
<td>
   1</td>
<td>
 6.000
</td>
<td>
 1.000
</td>
<td>
  .800
</td>
<td>
  .800
</td>
</tr>
<tr align="right">
<td>
   2</td>
<td>
 10.000
</td>
<td>
 4.000
</td>
<td>
  .100
</td>
<td>
  .100
</td>
</tr>
<tr align="right" bgcolor="#99FF99">
<td>
   3</td>
<td>
 1.000
</td>
<td>
 4.000
</td>
<td>
  .100
</td>
<td>
  .100
</td>
</tr>
<tr align="right">
<td>
   4</td>
<td>
 10.000
</td>
<td>
  .500
</td>
<td>
  .050
</td>
<td>
  .100
</td>
</tr>
<tr align="right" bgcolor="#99FF99">
<td>
   5</td>
<td>
 1.000
</td>
<td>
 4.000
</td>
<td>
  .100
</td>
<td>
  .100
</td>
</tr>
<tr align="right">
<td>
   6</td>
<td>
 1.000
</td>
<td>
 4.000
</td>
<td>
  .100
</td>
<td>
  .100
</td>
</tr>
<tr align="right" bgcolor="#99FF99">
<td>
   7</td>
<td>
 1.000
</td>
<td>
 4.000
</td>
<td>
  .100
</td>
<td>
  .100
</td>
</tr>
<tr align="right">
<td>
   8</td>
<td>
 1.000
</td>
<td>
 4.000
</td>
<td>
  .100
</td>
<td>
  .100
</td>
</tr>
<tr align="right" bgcolor="#99FF99">
<td>
   9</td>
<td>
 1.000
</td>
<td>
 4.000
</td>
<td>
  .100
</td>
<td>
  .100
</td>
</tr>
<tr align="right">
<td>
  10</td>
<td>
 1.000
</td>
<td>
 4.000
</td>
<td>
  .100
</td>
<td>
  .100
</td>
</tr>
</table>
<BR>
<BR>
<pre>
<!--#include file=frs:default.tlr -->