"use strict";

var bio = {
    "name": "Amit Vijairania",
    "role": "Software Engineer",
    "pic": "images/fry.jpg",
    "welcomeMessage": "Welcome to my online resume!",
    "contacts": {
        "mobile": "(415) 610.9908",
        "email": "amit.vijairania@gmail.com",
        "github": "avijaira",
        "location": "San Francisco, CA"
    },
    "skills": [
        "Developer",
        "JavaScript",
        "HTML",
        "CSS",
        "Go",
        "EmberJS"
    ]
};

var work = {
    "jobs": [
        {
            "employer": "Cisco Systems",
            "title": "Storage Architect",
            "location": "San Jose, CA",
            "dates": {
                "start": "2010",
                "end": "2014"
            },
            "description": "Storage Architect for Cisco IT. The implementation of the Internet of Everything (IoE) is leading to rapid innovation and business opportunity, along with new challenges for IT leaders. Many companies like yours are looking to improve business with new online services that foster growth while reducing costs, minimizing risks, and increasing agility. Multicloud environments are increasingly becoming the answer."
        },
        {
            "employer": "EMC",
            "title": "Systems Engineer",
            "location": "Boston, MA",
            "dates": {
                "start": "2004",
                "end": "2008"
            },
            "description": "Enterprise Systems Engineer. Whatever you need to do you can do it better than you ever knew possible with XtremIO. Database storage. VDI storage. Literally anything. Apps run faster. Scale better. Cost less. Gain tremendous flexibility. Empower users."
        }
    ]
};

var education = {
    "schools": [
        {
            "name": "UMass Lowell",
            "location": "Lowell, MA",
            "degree": "Master of Science",
            "major": "Computer Science",
            "dates": {
                "start": "2001",
                "end": "2003"
            },
            "url": "http://www.uml.edu"
        },
        {
            "name": "Maharshi Dayanand University",
            "location": "Rohtak, India",
            "degree": "Bachelor of Science",
            "major": "Computer Science",
            "dates": {
                "start": "1997",
                "end": "2001"
            },
            "url": "http://www.mdurohtak.ac.in"
        }
    ],
    "onlineCourses": [
        {
            "title": "Front-End Web Developer",
            "school": "Udacity",
            "dates": {
                "start": "2015",
                "end": "2015"
            },
            "url": "https://www.udacity.com"
        },
        {
            "title": "Full-Stack Web Developer",
            "school": "Udacity",
            "dates": {
                "start": "2015",
                "end": "2015"
            },
            "url": "https://www.udacity.com"
        }
    ]
};

var projects = [
    {
        "title": "Ceph",
        "dates": {
            "start": "2012",
            "end": "2015"
        },
        "description": "Ceph is a distributed object store and file system designed to provide excellent performance, reliability and scalability.",
        "image": "http://ceph.com/docs/master/_images/stack.png"
    },
    {
        "title": "OpenStack",
        "dates": {
            "start": "2013",
            "end": "2015"
        },
        "description": "OpenStack software controls large pools of compute, storage, and networking resources throughout a datacenter, managed through a dashboard or via the OpenStack API. OpenStack works with popular enterprise and open source technologies making it ideal for heterogeneous infrastructure.",
        "image": "https://www.openstack.org/themes/openstack/images/openstack-software-diagram.png"
    }
];

bio.display = function () {
    var m = HTMLmobile.replace("%data%", bio.contacts.mobile);
    var e = HTMLemail.replace("%data%", bio.contacts.email);
    var g = HTMLgithub.replace("%data%", bio.contacts.github);
    var l = HTMLlocation.replace("%data%", bio.contacts.location);
    $("#topContacts, #footerContacts").append(m, e, g, l);

    var r = HTMLheaderRole.replace("%data%", bio.role);
    var n = HTMLheaderName.replace("%data%", bio.name);
    $("#header").prepend(n, r);

    var p = HTMLbioPic.replace("%data%", bio.pic);
    var msg = HTMLwelcomeMsg.replace("%data%", bio.welcomeMessage);
    $("#header").append(p, msg);

    $("#header").append(HTMLskillsStart);
    bio.skills.forEach(function(skill) {
        var s = HTMLskills.replace("%data%", skill);
        $("#skills").append(s);
    });
    /* Alternate approach
    for (var i = 0; i < bio.skills.length; i++) {
        var skillName = HTMLskills.replace("%data%", bio.skills[i]);
        $("#skills").append(skillName);
    }
    */
};

work.display = function () {

    work.jobs.forEach(function(job) {
        $("#workExperience").append(HTMLworkStart);
        var je = HTMLworkEmployer.replace("%data%", job.employer);
        var jt = HTMLworkTitle.replace("%data%", job.title);
        var j = je + jt;
        $(".work-entry:last").append(j);
        var jd = job.dates.start + "  -  " + job.dates.end;
        var d = HTMLworkDates.replace("%data%", jd);
        $(".work-entry:last").append(d);
        var l = HTMLworkLocation.replace("%data%", job.location);
        $(".work-entry:last").append(l);
        var fd = HTMLworkDescription.replace("%data%", job.description);
        $(".work-entry:last").append(fd);
    });
};

projects.display = function () {

    projects.forEach(function(project) {
        $("#projects").append(HTMLprojectStart);
        var t = HTMLprojectTitle.replace("%data%", project.title);
        $(".project-entry:last").append(t);
        var pd = project.dates.start + "  -  " + project.dates.end;
        var d = HTMLprojectDates.replace("%data%", pd);
        $(".project-entry:last").append(d);
        var fd = HTMLprojectDescription.replace("%data%", project.description);
        $(".project-entry:last").append(fd);
        var i = HTMLprojectImage.replace("%data%", project.image);
        $(".project-entry:last").append(i);
    });
};

education.display = function () {

    education.schools.forEach(function(school) {
        $("#education").append(HTMLschoolStart);
        var n = HTMLschoolName.replace("%data%", school.name);
        $(".education-entry:last").append(n);
        var d = HTMLschoolDegree.replace("%data%", school.degree);
        $(".education-entry:last").append(d);
        var sd = school.dates.start + "  -  " + school.dates.end;;
        var d = HTMLschoolDates.replace("%data%", sd);
        $(".education-entry:last").append(d);
        var l = HTMLschoolLocation.replace("%data%", school.location);
        $(".education-entry:last").append(l);
        var m = HTMLschoolMajor.replace("%data%", school.major);
        $(".education-entry:last").append(m);
    });

    $("#education").append(HTMLonlineClasses);
    education.onlineCourses.forEach(function(course) {
        $("#education").append(HTMLonlineCoursesStart);
        var t = HTMLonlineTitle.replace("%data%", course.title);
        $(".online-entry:last").append(t);
        var s = HTMLonlineSchool.replace("%data%", course.school);
        $(".online-entry:last").append(s);
        var od = course.dates.start + "  -  " + course.dates.end;
        var d = HTMLonlineDates.replace("%data%", od);
        $(".online-entry:last").append(d);
        var u = HTMLonlineURL.replace("%data%", course.url);
        $(".online-entry:last").append(u);
    });
};

bio.display();
work.display();
projects.display();
education.display();

function locationizer(myWork) {

    if (myWork === undefined || myWork.jobs.length === 0) {
        return "I never had a job!";
    } else {
        var jobLocations = [];
        for (var i = 0; i < myWork.jobs.length; i++) {
            jobLocations.push(myWork.jobs[i].location);
        }
        return jobLocations;
    }
}
// Option 2: Add a function to String.prototype and you can chain it to other
// methods
String.prototype.capitalizeFirstLetter = function() {
    // string => String
    // Avoid undefined for empty string
    return this && this.charAt(0).toUpperCase() + this.slice(1).toLowerCase();
}

function inName(fullName) {

    if (fullName === undefined) {
        console.log("No Full name passed for Internationalization");
    } else {
        var names = fullName.trim().split(" ");
        if (names.length !== 2) {
            console.log("Full name doesn't include First and Last name");
        } else {
            var iName = names[0].capitalizeFirstLetter() + " " + names[1].toUpperCase();
            return iName;
        }
    }
}

$(document).ready(function() {
  $('button').click(function() {
    var iName = inName(bio.name) || function(){};
    $('#name').html(iName);
  });
});

//$("#main").append(internationalizeButton);
$("#mapDiv").append(googleMap);
