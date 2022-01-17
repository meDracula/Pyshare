db.createUser({
	user: "albin",
	pwd: "password",
	roles: [
		{
		role: "readWrite",
		db: "pysharedb",
		},
		]
	}
);
