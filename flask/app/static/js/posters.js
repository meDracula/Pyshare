function upvote(input) {
	const params = { title_hash: input.value, vote: 1 };
	let id = "rate-"+input.value;

	fetch("http://127.0.0.1/ajax/post_vote", {
		method: 'POST',
		headers: { 'Content-type': 'application/json' },
		body: JSON.stringify(params)
		})
		.then(response => {
			if (response.status == 200) {
				return response.json();
			}
		}).then(msg => {
			document.getElementById(id).innerHTML = msg.rating;
		})
		.catch(error => {
			alert(error)
		});
}

function downvote(input) {
	const params = { title_hash: input.value, vote: -1 };
	let id = "rate-"+input.value;

	fetch("http://127.0.0.1/ajax/post_vote", {
		method: 'POST',
		headers: { 'Content-type': 'application/json' },
		body: JSON.stringify(params)
		})
		.then(response => {
			if (response.status == 200) {
				return response.json();
			}
		})
		.then(msg => {
			document.getElementById(id).innerHTML = msg.rating;
		})
		.catch(error => {
			alert(error)
		});
}

function pressEnter(input) {
	if (event.keyCode == 13) {
		this.form.submit();
	}
	return false;
}
