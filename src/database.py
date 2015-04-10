import _mysql
import sys

class database(object):

    def __init__(self):
        try:
            self.con = _mysql.connect('ephesus.cs.cf.ac.uk' , 'c1312433', 'berlin', 'c1312433')
        except _mysql.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)

    def add_user(self, path_to_face, passphrase, first_name, last_name, groups, rooms):
        crs = con.cursor()
        crs.execute("INSERT INTO user_records(user_id, forename, surname, photo_file, audio_file, specified_rooms, permitted_groups) VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%s')") % rand_no

    def update_user(self, user_id):

    def exit(self):
        self.con.close()

