window.onload=initall;
var saveAnsButton;
function initall()
{
  saveAnsButton=document.getElementById('save_ans')
  saveAnsButton.onclick=saveans
}
function saveans()
{
  var ans=$("input:radio[name=name]:checked").val()
    document.getElementById("submitAnswer").disabled = false;
  document.getElementById("save_ans").disabled = true;
  alert("ANSWER IS SUBMITED CLICK 'NEXT' TO CONTINUE")


var req=new XMLHttpRequest();

var url='/saveans?ans='+ans
req.open("GET",url,true)
req.send()
}