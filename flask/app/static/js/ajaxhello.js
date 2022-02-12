function hello() {
	fetch("http://127.0.0.1/ajax/helloworld")
		.then(response => response.json())
		.then(msg => console.log(msg))
		.catch(error => alert(error));
}

