started = false;

document.body.onclick = function () {

    spanz = document.getElementsByTagName("span");
    v_count = 0

    for(var i=0;i< spanz.length;i++) {
        console.log(spanz[i].getAttribute("interval_id"))

        if(spanz[i].getAttribute("interval_id") != "0") {
            v_count++ 
        }
    }

    console.log(v_count)
    console.log(document.getElementsByTagName("SPAN").length)

    if(v_count === document.getElementsByTagName("SPAN").length ) {

        console.log("app start")
        started=true

    } else {

        started=false
    }

    console.log("started" + started)

    if(started===true) {
        v_count = 0

        for(var i=0;i< spanz.length;i++) {

            appstart(spanz[i].getAttribute("id"))
        }

        started = false

    } else {

        console.log("app start")

        for(var i=0;i< spanz.length;i++) {


            appstart(spanz[i].getAttribute("id"))
        }
    }
}