function ColorTool(index) {
    
           document.getElementsByTagName("span")[index].setAttribute("running","true")
           var toolObject = {}
        

            {
                toolObject.interval = 0
                toolObject.colors   =  ["white","silver","grey","red","maroon","yellow","olive","lime","green","aqua","teal","blue","navy","fuchsia","purple","white"]
                /*["white","silver","grey","black","grey", "silver","white"]*/
                /* color definition --> ["white","silver","grey","red","maroon","yellow","olive","lime","green","aqua","teal","blue","navy","fuchsia","purple","white"]*/
                toolObject.count    =  toolObject.colors.length
                function changeColor () { 

                        console.log("things are changing on count " + toolObject.count)

                        toolObject.count            = toolObject.count - 1
                        returnColor                 = toolObject.colors[0]

                        if(toolObject.count > -1 ) {

                                if(toolObject.colors[toolObject.colors.indexOf(document.getElementsByTagName("span")[index].style.backgroundColor) + 1] === undefined){

                                        returnColor = toolObject.colors[0]

                                } else {

                                        returnColor = toolObject.colors[toolObject.colors.indexOf(document.getElementsByTagName("span")[index].style.backgroundColor) + 1]
                                }


                        document.getElementsByTagName("span")[index].style.backgroundColor = returnColor

                        } else {
                                /* 1. Stop the count down 
                                   2. Update the running status
                                   3. Check undefined
                                */

                                clearInterval(toolObject.interval)
                                document.getElementsByTagName("span")[index].setAttribute("running","false")
                                if(document.getElementsByTagName("span")[index+1] != undefined) {

                                                ColorTool(index+1)
                                } 
                                
                        

                        }

                }

                toolObject.interval = setInterval(function() { changeColor() },10)     
                
                console.log("return value " + document.getElementsByTagName("span")[index].getAttribute("id"))

                return document.getElementsByTagName("span")[index].getAttribute("id")
                        }
                
                
                }

thisid = ColorTool(1)
console.log(thisid);



console.log("scrathpad")