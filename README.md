### Supervisord examples

This has live demos to demonstrate the effects of supervisord config.
See the docs at:

http://supervisord.org/configuration.html

The command to run this in the foreground is this:

```
supervisord --pidfile=./supervisor_pid --configuration=demo.conf --nodaemon
```

While you have that running, you should check on it in another tab:

```
supervisorctl --configuration=demo.conf status
```

That should give output like this:

```
$ supervisorctl --configuration=demo.conf status
fail-slowly                      RUNNING   pid 1022768, uptime 0:00:03
fail-too-fast                    FATAL     Exited too quickly (process log may have details)
fail-zero                        RUNNING   pid 1022789, uptime 0:00:00
```

You probably want to run this in a virtual environment, I used `python script.py`
type of invocation in order to be agnostic to your python environment.
