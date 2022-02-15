function upvote(input) {
	const params = { title_hash: input.value, vote: 1 };
	let id = "rate-"+input.value;
	let score = parseInt(document.getElementById(id).innerHTML);

	fetch("http://127.0.0.1/ajax/post_vote", {
		method: 'POST',
		headers: { 'Content-type': 'application/json' },
		body: JSON.stringify(params)
		})
		.then(response => {
			if(response.status == 400) {
				return Promise.reject("Code tampering");
			}
			else if (response.status == 200) {
				score += 1;
				document.getElementById(id).innerHTML = score.toString();
			}
		})
		.catch(error => {
			alert(error)
		});
}

function downvote(input) {
	const params = { title_hash: input.value, vote: -1 };
	let id = "rate-"+input.value;
	let score = parseInt(document.getElementById(id).innerHTML);

	fetch("http://127.0.0.1/ajax/post_vote", {
		method: 'POST',
		headers: { 'Content-type': 'application/json' },
		body: JSON.stringify(params)
		})
		.then(response => {
			if(response.status == 400) {
				return Promise.reject("Code tampering");
			}
			else if (response.status == 200) {
				score -= 1;
				document.getElementById(id).innerHTML = score.toString();
			}
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
