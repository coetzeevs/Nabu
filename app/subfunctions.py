def searcher():
	from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
	if request.method == 'POST':
		if request.form['btn'] == 'Bar_SCV':
	    		barname = request.form['barishname']
	    		return redirect('http://0.0.0.0:4000/profile/{0}'.format(barname))
