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
        crs.execute("INSERT INTO user_records(forename, surname, photo_file, audio_file, specified_rooms, permitted_groups) VALUES(%d, %s, %s, %s, %s, %s, %s)") % (first_name, last_name, path_to_face, passphrase, rooms, groups )
        user_id = crs.execute("SELECT user_id FROM user_records WHERE photo_file=%s, audio_file=%s") % (path_to_face, passphrase)
        crs.execute("INSERT INTO user_locate(user_id, forename, surname, room, access_time) VALUES (%d, %s, %s, 0, 0)")

    def update_user(self, room, user_id):
        current_time = time.strftime("%H:%M:%S")
        crs = con.cursor()
        crs.execute("UPDATE user_locate SET room=%s, access_time=%s WHERE user_id=%d") % (room, current_time, user_id)
        
    def exit(self):
        self.con.close()

