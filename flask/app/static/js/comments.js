function commentShow() {
	if (document.getElementById('comments').style.visibility === "hidden") {
		document.getElementById('comments').style.visibility = "visible";
	}
	else {
		console.log("visible")
		document.getElementById('comments').style.visibility = "hidden";
	}
}
