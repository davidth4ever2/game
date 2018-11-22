

window.colors = ["white","silver",
                "grey","red",
                "maroon","yellow",
                "olive","lime",
                "green","aqua",
                "teal","blue",
                "navy","fuchsia",
                "purple"
            ]
var intervalID = 0



function appstart(containerID) {

    intervalID = setInterval(function() {
                    document.getElementById(new String(containerID)).style.backgroundColor = "rgb(" +  Math.floor(Math.random() * 255) +"," +  Math.floor(Math.random() * 255) +"," +  Math.floor(Math.random() * 255) +  ")"
                    document.getElementById(new String(containerID)).innerText             = Math.floor(Math.random() * 10)
                }, 
                Math.floor(Math.random() * 3000))
                
                document.getElementById(new String(containerID)).setAttribute("interval_id",intervalID)     
            }



function appstop(containerID) {

    clearInterval(document.getElementById(containerID).getAttribute("interval_id"))
}
           

            