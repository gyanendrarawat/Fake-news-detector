function show(event) {
    var t = document.getElementById("i1").value;
    if (t == "") {
      console.log("nothing happens");
      return event.preventDefault();
    }

    console.alert('done');
  }
  
  function close(event) {
    var c = document.getElementById("pred");
    c.style.display = "none";
  }
  
  
  
  
  let btn = document.getElementById("btn");
  btn.addEventListener("click", show);
  
  let clz = document.getElementById("close").addEventListener("click", close);
  

