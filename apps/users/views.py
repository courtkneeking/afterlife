from django.shortcuts import render, redirect
from .models import * 

def index(request):
	subjects = Subject.objects.all()
	context = {
		"subjects" : subjects
	}
	return render(request, "users/index.html", context)

def add(request):
	return render(request, "users/add.html")

def submit(request):
	
	subject = Subject.objects.create(subject_name = request.POST['subject_name'], birthday = request.POST['birthday'], death_date = request.POST['death_date'], profile_image = request.POST['profile_image'], slideshow = request.POST['slideshow'], gofundme = request.POST['gofundme'])
	obituary = Obituary.objects.create(obituary_image = request.POST['obituary_image'], subject_description = request.POST['subject_description'], subject_family = request.POST['subject_family'], funeral_information = request.POST['funeral_information'])
	subject.obituaries.add(obituary)
	request.session['subject_id'] = subject.id
	return redirect('/display/{}'.format(subject.id))

def display(request, subject_id):
	subject = Subject.objects.get(id = subject_id)
	stories = subject.stories.all()
	condolences = subject.condolences.all()
	friends = subject.friends.all()
	images = subject.images.all()
	obituary = Obituary.objects.get(subject_id = subject.id)
	context = {
		"subject" : subject,
		"stories" : stories,
		"condolences" : condolences,
		"friends" : friends,
		"images" : images,
		"obituary" : obituary
	}
	return render(request, "users/display.html", context)

def addfriend(request):
	subject_id = request.session['subject_id']
	subject = Subject.objects.get(id = subject_id)
	friend = Friend.objects.create(name = request.POST['name'], email = request.POST['email'])
	subject.friends.add(friend)
	return redirect('/display/{}#info'.format(subject_id))

def addcondolence(request):
	subject_id = request.session['subject_id']
	subject = Subject.objects.get(id = subject_id)
	condolence = Condolence.objects.create(condolence = request.POST['condolence'], author = request.POST['author'])
	subject.condolences.add(condolence) 
	return redirect('/display/{}#info'.format(subject_id))

def addstory(request):
	subject_id = request.session['subject_id']
	subject = Subject.objects.get(id = subject_id)
	story = Story.objects.create(story = request.POST['story'], author = request.POST['author'])
	subject.stories.add(story)
	return redirect('/display/{}#memories'.format(subject_id))

def addimage(request):
	subject_id = request.session['subject_id']
	subject = Subject.objects.get(id = subject_id)
	image = Image.objects.create(image = request.POST['image'])
	subject.images.add(image)
	return redirect('/display/{}#memories'.format(subject_id))

def edit(request, subject_id):
	request.session['subject_id'] = subject_id
	subject = Subject.objects.get(id = subject_id)
	stories = subject.stories.all()
	condolences = subject.condolences.all()
	friends = subject.friends.all()
	images = subject.images.all()
	obituary = Obituary.objects.get(subject_id = subject.id)
	context = {
		"subject" : subject,
		"stories" : stories,
		"condolences" : condolences,
		"friends" : friends,
		"images" : images,
		"obituary" : obituary
	}
	return render(request, "users/edit.html", context)

def deletestory(request):
	subject_id = request.session['subject_id']
	subject = Subject.objects.get(id = subject_id)
	story = Story.objects.get(id = request.POST["story"])
	story.delete()
	return redirect('/display/{}'.format(subject_id))

def deleteimage(request):
	subject_id = request.session['subject_id']
	subject = Subject.objects.get(id = subject_id)
	image = Image.objects.get(id = request.POST['image'])
	image.delete()
	return redirect('/display/{}'.format(subject_id))


def deletefriend(request):
	subject_id = request.session['subject_id']
	subject = Subject.objects.get(id = subject_id)
	friend = Friend.objects.get(id = request.POST['friend'])
	friend.delete()
	return redirect('/display/{}'.format(subject_id))

def deletecondolence(request):
	subject_id = request.session['subject_id']
	subject = Subject.objects.get(id = subject_id)
	condolence = Condolence.objects.get(id = request.POST['condolence'])
	condolence.delete()
	return redirect('/display/{}'.format(subject_id))

def editpage(request):
	subject_id = request.session['subject_id']
	subject = Subject.objects.get(id = subject_id)
	obituary = Obituary.objects.get(subject_id = subject_id)
	# if len(request.POST['profile_image']) > 1:
	# 	subject.profile_image = request.POST['profile_image']
	if len(request.POST['subject_name']) > 1: 
		subject.subject_name = request.POST['subject_name']
		subject.save()
	if len(request.POST['birthday']) > 1: 
		subject.birthday = request.POST['birthday']
		subject.save()
	if len(request.POST['death_date']) > 1:
		subject.death_date = request.POST['death_date']
		subject.save()
	if len(request.POST['slideshow']) > 1: 
		subject.slideshow = request.POST['slideshow']
		subject.save()
	if len(request.POST['gofundme']) > 1:
		subject.gofundme = request.POST['gofundme']
		subject.save()
	if len(request.POST['obituary_image']) > 1:
		obituary.obituary_image = request.POST['obituary_image']
		obituary.save()
	if len(request.POST['subject_description']) > 1:
		obituary.subject_description = request.POST['subject_description']
		obituary.save()
	if len(request.POST['subject_family']) > 1:
		obituary.subject_family = request.POST['subject_family']
		obituary.save()
	if len(request.POST['funeral_information']) > 1: 
		obituary.funeral_information = request.POST['funeral_information']
		obituary.save()
	return redirect('/display/{}'.format(subject_id))

def displayslideshow(request):
	return render(request, "users/slideshow.html")	





