function populatePage(containerID) {

    this_document = document.getElementById( new String(containerID) )

    for(var i=0;i<10;i++) { 

        if(i%120!=0) {

          span_new    = document.createElement("SPAN")
          span_test   = document.createTextNode(new String( Math.floor( Math.random() * 10 ) ))
          span_new.id = containerID + i
          span_new.appendChild(span_test)
          this_document.appendChild(span_new)
          
        } else {

          sectionBreak = document.createElement("BR")
          this_document.appendChild(sectionBreak)
        }
    }

    console.log("finished loading")
}



