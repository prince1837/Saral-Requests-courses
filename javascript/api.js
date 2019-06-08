const axios=require("axios")
const read=require("readline-sync")
var data=axios.get("http://saral.navgurukul.org/api/courses")
.then((response)=>{
	var my_data=(response.data.availableCourses)
	var empty=[]
	var a=0
	for (i of my_data){
		a++
		console.log(a,i.name)
		empty.push(i.id)
	} 
	input=read.question()
	var my_id=empty[input-1]
	var new_url="http://saral.navgurukul.org/api/courses/"+my_id.toString()+"/exercises"
	var data1=axios.get(new_url)
	.then((response)=>{
		var my_data1=(response.data.data)
		var a=0
		var slug=[]
		for(i of my_data1){
			a++
			console.log(a,i.name)
			slug.push(i.slug)
		}
		input1=read.question()
		console.log(input1)
		var my_id1=slug[input1-1]
		new_url1="http://saral.navgurukul.org/api/courses/"+my_id.toString()+"/exercise/getBySlug?slug="+my_id1.toString()
		var data2=axios.get(new_url1)
		.then((response)=>{
			var my_data2=(response.data.content)
			console.log(my_data2)
		})
		.catch((error)=>{
		console.log("error ayega")
		});

	})
	.catch((error)=>{
	console.log("error ayega")
	});
})
.catch((error)=>{
	console.log("error ayega")
});
