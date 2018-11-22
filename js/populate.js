function populatePage(containerID) {

    console.log(containerID)
    this_document = document.getElementById( new String(containerID) )
    console.log(this_document)
    

    for(var i=0;i<1000;i++) { 

        if(i%120!=0) {

          span_new    = document.createElement("SPAN")
          span_test   = document.createTextNode(new String( Math.floor( Math.random() * 10 ) ))
          span_new.id = containerID + i
          span_new.appendChild(span_test)
          this_document.appendChild(span_new)
          
          /*script_new  = document.createElement("SCRIPT")
          script_text = document.createTextNode( "app('" + containerID + "')")
          script_new.appendChild(script_text)
          this_document.appendChild(script_new)*/



        } else {

          sectionBreak = document.createElement("BR")
          this_document.appendChild(sectionBreak)
        }
    }

    console.log("finished loading")
}

populatePage("container0")

