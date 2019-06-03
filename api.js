const axios = require('axios');
const fs = require('fs');
const readline = require('readline-sync')

// checking the existance of json file if not exist then create new json file by requesting the api and store the data.
// if the json file exists then it prefer `else` condition and read the json file and use the data in other processses
fs.exists(__dirname+'/courses.json',(exists)=>{
    if(!exists){
        axios
        .get("http://saral.navgurukul.org/api/courses")
        .then(function (response){
            var data = response.data
            fs.writeFileSync("courses.json",JSON.stringify(data,null,2))
        })
        .catch(function(error){
            console.log(error.response.status)
        }
        )
    }else{
    var data = fs.readFileSync('courses.json')
    data = JSON.parse(data)
    for(var i of data.availableCourses){
        var courses = data.availableCourses.indexOf(i) + " " + i.name
        console.log(courses)
    }
    console.log()
    //taking input from the user and asking to select any of index of the course from user
    // and resulting the exercises of that courses as output with index
    var user = readline.question("Enter the index of course : ")
    axios
    .get("http://saral.navgurukul.org/api/courses/"+ data.availableCourses[user].id +"/exercises")
    .then(function (response){
        var exerciseData = response.data.data
        // printing the exercises with index
        if(exerciseData.length>0){
            for (var j of exerciseData){
                var exercise = exerciseData.indexOf(j)+ ' ' + j.name 
                console.log(exercise)
                // printing the childExercise with parentIndex.index below-with their parent exercise
                for (var k of j.childExercises){
                    console.log("      ",exerciseData.indexOf(j)+'.'+j.childExercises.indexOf(k) ,k.name)
                }
                console.log()
            }
            // taking input from the user to printing the api data of either exercise or the childExercises
            var user1=readline.question("Enter the index of exercise :")
            user1=user1.split('.')

                if (user1.length>1){
                        user2=user1[1]
                        // console.log(user1)
                        console.log()
                        axios
                        .get("http://saral.navgurukul.org/api/courses/"+user+"/exercise/getBySlug?slug="+exerciseData[user1[0]].childExercises[user2].slug)
                        .then(function (response){
                            console.log(response.data)
                        })
                    }else{
                        axios
                        .get("http://saral.navgurukul.org/api/courses/"+user+"/exercise/getBySlug?slug="+exerciseData[user1[0]].slug)
                        .then(function (response){
                            console.log(response.data)
                        })
                    }
        }else{
            console.log("\n       Your course has no any exercise\n")
            }
        })
    }
})
