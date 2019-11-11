Then install dependencies and check that it works

```bash
$ make server.install      # Install the pip dependencies on the docker container
$ make server.start        # Run the container containing your local python server
$ make database.upgrade
```

If everything works, you should see the available routes [here](http://127.0.0.1:3000/spec).

