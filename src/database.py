import MySQLdb
import sys
import time

class database(object):

    def __init__(self):
        try:
            self.con = MySQLdb.connect('ephesus.cs.cf.ac.uk' , 'c1312433', 'berlin', 'c1312433')
            print "success"
        except _mysql.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)

    def add_user(self, path_to_face, passphrase, first_name, last_name, groups, rooms):
        crs = self.con.cursor()
        ids,names = self.get_rooms_from_groups()
        query = "INSERT INTO user_records(forename, surname, photo_file, audio_file, specified_rooms) VALUES('%s','%s','%s','%s','%s','%s');" % (first_name,last_name,path_to_face,passphrase,(rooms+str(names.strip('[]'))))
        crs.execute(query)
        query = "SELECT user_id FROM user_records WHERE photo_file='%s' AND audio_file='%s';" % (path_to_face, passphrase)
        user_id = crs.execute(query)
        crs.execute("INSERT INTO user_locate(user_id, forename, surname, room, access_time) VALUES ('%d', '%s', '%s', 0, 0);" % (user_id,first_name,last_name))


    def update_user(self, user_id, room=1):
        current_time = time.strftime("%H:%M:%S")
        crs = self.con.cursor()
        crs.execute("UPDATE user_locate SET room='%s', access_time='%s' WHERE user_id='%d';"% (room, current_time, user_id)) 

    def verify(self,path_to_face, passphrase, room):
        crs = self.con.cursor()
        query = "SELECT user_groups.rooms,user_records.specified_rooms FROM user_records INNER JOIN user_groups WHERE user_records.photo_file='%s' AND user_records.audio_file='%s';" % (path_to_face, passphrase)
        rooms = []
        rooms.append(crs.execute(query))
        print path_to_face+passphrase
        print rooms
        if room not in rooms:
            print "aayyy"
            return False
        else:
            print "hi"
            return True

    def get_groups(self):
        crs = self.con.cursor()
        groups = "SELECT DISTINCT group_name,group_id FROM user_groups WHERE 1"
        row = crs.execute(groups)
        rows = crs.fetchall()
        i = 0
        group_id = []
        group_name = []
        for row in rows:
            group_name.append(row[0])
            group_id.append(row[1])
            i+=1
        return group_id,group_name

    def get_rooms(self):
        crs = self.con.cursor()
        rooms = "SELECT DISTINCT room_name,room_id FROM room_lookup WHERE 1"
        row= crs.execute(rooms)
        rows = crs.fetchall()
        i = 0
        room_id = []
        room_name = []
        for row in rows:
            print row
            room_name.append(row[0])
            room_id.append(row[1])
            i+=1
        return room_id,room_name

    def get_rooms_from_groups(self):
        crs = self.con.cursor()
        rooms = "SELECT DISTINCT room_lookup.room_name,room_lookup.room_id FROM room_lookup INNER JOIN user_groups WHERE user_groups.group_name = '%s'"
        row= crs.execute(rooms)
        rows = crs.fetchall()
        i = 0
        room_id = []
        room_name = []
        for row in rows:
            print row
            room_name.append(row[0])
            room_id.append(row[1])
            i+=1
        return room_id,room_name

    def exit(self):
        self.con.close()

