#!/usr/bin/env python

"""
populate.py: Python script written to populate the Trip_Detail, Water_Craft, & Trip_Package tables
in DB used in CS50W-2020 Final Project. Some data obtained from `https://frontroyaloutdoors.com/`.
This script needs to be run from the same Django environment where website is being loaded. It
required the `django-extensions` module be installed, & `django_extensions` added to
`INSTALLED_APPS` in `settings.py. Script must be placed in `<project_root>/scripts`. It is then run
with the `python manage.py runscript populate` command.
"""

# Model imports
from riverRent.models import Trip_Detail, Water_Craft, Trip_Package

def run():
    # Import Trip_Detail
    Trip_Detail.objects.bulk_create([
        
        Trip_Detail(Trip_Number = "1", Put_In = "Karo Landing", Take_Out = "Front Royal Outdoors"
            , Distance = "3", Time_Desc = "1 to 2 (Tube: 3 to 4) Hours", Final_Start_Time = "14:30"
            , Description = "Trip 1 floats from Karo Landing, river mile marker 37, downstream 3 "
            "miles to our base at Front Royal Outdoors, river mile marker 40."
            , Trip_Category = "short", Level = "any level"),
        Trip_Detail(Trip_Number = "2", Put_In = "Karo Landing", Take_Out = "Front Royal Landing"
            , Distance = "7", Time_Desc = "2 to 4 Hours", Final_Start_Time = "13:00"
            , Description = "Trip 2 floats from Karo Landing, river mile marker 37, downstream 7 "
            "miles to Front Royal Landing, river mile marker 44."
            , Trip_Category = "short", Level = "any level"),
        Trip_Detail(Trip_Number = "3", Put_In = "Bentonville Landing", Take_Out = "Front Royal " 
            "Outdoors", Distance = "11.5", Time_Desc = "4 to 6 Hours", Final_Start_Time = "12:30"
            , Description = "Popular full-day trip with above normal river level. Trip 3 floats "
            "from Bentonville Landing, river mile marker 28, downstream 11.5 miles to our base at "
            "Front Royal Outdoors, river mile marker 40.", Trip_Category = "long"
            , Level = "1.8′ or higher"),
        Trip_Detail(Trip_Number = "4", Put_In = "Seekford Landing", Take_Out = "Bentonville "
            "Landing", Distance = "12", Time_Desc = "4 to 6 Hours", Final_Start_Time = "12:00"
            , Description = "Popular full-day trip. Trip 4 floats from Seekfords Landing, river "
            "mile marker 16, downstream 12 miles to Bentonville Landing, river mile marker 28."
            , Trip_Category = "long", Level = "any level"),
        Trip_Detail(Trip_Number = "5", Put_In = "Bentonville Landing", Take_Out = "Front Royal "
            "Landing", Distance = "16", Time_Desc = "5 to 6 Hours", Final_Start_Time = "11:00"
            , Description = "Trip 5 floats from Bentonville Landing, river mile marker 28, "
            "downstream 16 miles to Front Royal Landing, river mile marker 44."
            , Trip_Category = "long", Level = "1.8′ or higher"),
        Trip_Detail(Trip_Number = "6", Put_In = "Bealers Ferry", Take_Out = "Bentonville Landing"
            , Distance = "19", Time_Desc = "6 to 7 Hours", Final_Start_Time = "11:00"
            , Description = "Trip 6 floats from Bealers Ferry Landing, river mile marker 9, "
            "downstream 19 miles to Bentonville Landing, river mile marker 28."
            , Trip_Category = "long", Level = "1.8′ or higher"),
        Trip_Detail(Trip_Number = "7", Put_In = "Seekford Landing", Take_Out = "Front Royal "
            "Outdoors", Distance = "23.5", Time_Desc = "2 Days", Final_Start_Time = "12:00"
            , Description = "Good multi-day trip. Trip 7 is a two-day trip that floats from "
            "Seekford Landing, river mile marker 16, downstream 23.5 miles to our base at Front "
            "Royal Outdoors, river mile marker 40.", Trip_Category = "multi"
            , Level = "1.8′ or higher"),
        Trip_Detail(Trip_Number = "7A", Put_In = "Inskeep Landing", Take_Out = "Bentonville "
            "Landing", Distance = "28", Time_Desc = "2 Days", Final_Start_Time = "12:00"
            , Description = "Trip 7A is a two-day trip that floats from Bixler Bridge Landing, "
            "river mile marker 0, downstream 28 miles to Bentonville Landing, river mile marker 28."
            , Trip_Category = "multi", Level = "1.8′ or higher"),
        Trip_Detail(Trip_Number = "8", Put_In = "Inskeep Landing", Take_Out = "Front Royal "
            "Outdoors", Distance = "40", Time_Desc = "3 Days", Final_Start_Time = "12:00"
            , Description = "Trip 8 is a three-day trip that floats from Bixler Bridge Landing, "
            "river mile marker 0, downstream 40 miles to our base at Front Royal Outdoors, river "
            "mile marker 40.", Trip_Category = "multi", Level = "1.8′ or higher"),
        Trip_Detail(Trip_Number = "SP1", Put_In = "Bentonville Landing", Take_Out = "State Park"
            , Distance = "3.5", Time_Desc = "1 to 2 Hours", Final_Start_Time = "15:00"
            , Description = "State Park Trip 1 floats from Bentonville Landing, river mile marker "
            "28, downstream 3.5 miles to the Shenandoah River State Park, river mile marker 31.5."
            , Trip_Category = "short", Level = "any level"),
        Trip_Detail(Trip_Number = "SP2", Put_In = "State Park", Take_Out = "Karo Landing"
            , Distance = "5", Time_Desc = "2 to 3 Hours", Final_Start_Time = "12:30"
            , Description = "State Park Trip 2 floats from the Shenandoah River State Park, river "
            "mile marker 31.5, downstream 5 miles to Karo Landing, river mile marker 37."
            , Trip_Category = "short", Level = "1.8′ or higher"),
        Trip_Detail(Trip_Number = "SP3", Put_In = "State Park", Take_Out = "Front Royal Outdoors"
            , Distance = "8", Time_Desc = "3 to 4 Hours", Final_Start_Time = "12:30"
            , Description = "State Park Trip 3 floats from State Park to Front Royal Outdoors."
            , Trip_Category = "long", Level = "1.8′ or higher"),
        Trip_Detail(Trip_Number = "SP4", Put_In = "State Park", Take_Out = "Front Royal Landing"
            , Distance = "12", Time_Desc = "4 to 6 Hours", Final_Start_Time = "12:00"
            , Description = "State Park Trip 4 floats from Shenandoah River State Park, river "
            "mile marker 31.5, downstream 12 miles to Front Royal Landing, river mile marker 44."
            , Trip_Category = "long", Level = "1.8′ or higher"),
        Trip_Detail(Trip_Number = "SP5", Put_In = "Burners Ford", Take_Out = "Front Royal "
            "Outdoors", Distance = "18.5", Time_Desc = "2 Days", Final_Start_Time = "12:00"
            , Description = "State Park Trip 5 is a two-day trip that floats from Burners Ford "
            "Landing, river mile marker 21, downstream 18.5 miles to our base at Front Royal "
            "Outdoors, river mile marker 40.", Trip_Category = "multi", Level = "1.8′ or higher"),
        Trip_Detail(Trip_Number = "SP6", Put_In = "Ruffners Camp", Take_Out = "Front Royal "
            "Outdoors", Distance = "34", Time_Desc = "3 Days", Final_Start_Time = "12:00"
            , Description = "State Park Trip 6 is a three-day trip that floats from Ruffners "
            "Landing, river mile marker 6, downstream 34 miles to our base at Front Royal "
            "Outdoors, river mile marker 40.", Trip_Category = "multi", Level = "1.8′ or higher"),
    ])
    
    # Import Water_Craft
    Water_Craft.objects.bulk_create([
        
        Water_Craft(Type = "Canoe", Count = "100"),
        Water_Craft(Type = "Solo Kayak", Count = "87"),
        Water_Craft(Type = "Tandem Kayak", Count = "24"),
        Water_Craft(Type = "Fishing Kayak", Count = "18"),
        Water_Craft(Type = "4-Man Raft", Count = "18"),
        Water_Craft(Type = "6-Man Raft", Count = "12"),
        Water_Craft(Type = "Stand-Up Paddle Board", Count = "12"),
        Water_Craft(Type = "Tube", Count = "314"),
    ])

    # Import Trip_Package
    Trip_Package.objects.bulk_create([
        
        # Canoe packages
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Canoe"), Trip = Trip_Detail.objects.get(Trip_Number="1"), Price = "50"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Canoe"), Trip = Trip_Detail.objects.get(Trip_Number="2"), Price = "60"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Canoe"), Trip = Trip_Detail.objects.get(Trip_Number="3"), Price = "65"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Canoe"), Trip = Trip_Detail.objects.get(Trip_Number="4"), Price = "65"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Canoe"), Trip = Trip_Detail.objects.get(Trip_Number="5"), Price = "67"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Canoe"), Trip = Trip_Detail.objects.get(Trip_Number="6"), Price = "71"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Canoe"), Trip = Trip_Detail.objects.get(Trip_Number="7"), Price = "115"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Canoe"), Trip = Trip_Detail.objects.get(Trip_Number="7A"), Price = "125"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Canoe"), Trip = Trip_Detail.objects.get(Trip_Number="8"), Price = "150"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Canoe"), Trip = Trip_Detail.objects.get(Trip_Number="SP1"), Price = "58"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Canoe"), Trip = Trip_Detail.objects.get(Trip_Number="SP2"), Price = "62"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Canoe"), Trip = Trip_Detail.objects.get(Trip_Number="SP3"), Price = "62"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Canoe"), Trip = Trip_Detail.objects.get(Trip_Number="SP4"), Price = "67"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Canoe"), Trip = Trip_Detail.objects.get(Trip_Number="SP5"), Price = "125"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Canoe"), Trip = Trip_Detail.objects.get(Trip_Number="SP6"), Price = "155"),
        
        # Solo Kayak packages
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Solo Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="1"), Price = "38"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Solo Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="2"), Price = "43"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Solo Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="3"), Price = "46"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Solo Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="4"), Price = "46"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Solo Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="5"), Price = "49"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Solo Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="6"), Price = "51"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Solo Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="7"), Price = "78"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Solo Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="7A"), Price = "84"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Solo Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="8"), Price = "99"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Solo Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP1"), Price = "42"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Solo Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP2"), Price = "46"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Solo Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP3"), Price = "46"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Solo Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP4"), Price = "49"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Solo Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP5"), Price = "84"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Solo Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP6"), Price = "104"),
        
        # Tandem Kayak packages
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Tandem Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="1"), Price = "50"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Tandem Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="2"), Price = "60"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Tandem Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="3"), Price = "65"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Tandem Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="4"), Price = "65"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Tandem Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="5"), Price = "67"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Tandem Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="6"), Price = "71"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Tandem Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="7"), Price = "115"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Tandem Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="7A"), Price = "125"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Tandem Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="8"), Price = "150"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Tandem Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP1"), Price = "58"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Tandem Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP2"), Price = "62"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Tandem Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP3"), Price = "62"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Tandem Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP4"), Price = "67"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Tandem Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP5"), Price = "125"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Tandem Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP6"), Price = "155"),
        
        # Fishing Kayak packages
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Fishing Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="1"), Price = "58"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Fishing Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="2"), Price = "63"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Fishing Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="3"), Price = "66"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Fishing Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="4"), Price = "66"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Fishing Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP1"), Price = "66"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Fishing Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP2"), Price = "66"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Fishing Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP3"), Price = "66"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Fishing Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP4"), Price = "66"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Fishing Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP5"), Price = "104"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Fishing Kayak"), Trip = Trip_Detail.objects.get(Trip_Number="SP6"), Price = "124"),
        
        # 4-Man Raft packages
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="4-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="1"), Price = "110"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="4-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="2"), Price = "120"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="4-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="3"), Price = "125"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="4-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="4"), Price = "125"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="4-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="5"), Price = "129"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="4-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="6"), Price = "137"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="4-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="7"), Price = "225"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="4-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="7A"), Price = "245"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="4-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="8"), Price = "295"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="4-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="SP1"), Price = "115"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="4-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="SP2"), Price = "125"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="4-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="SP3"), Price = "125"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="4-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="SP4"), Price = "130"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="4-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="SP5"), Price = "245"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="4-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="SP6"), Price = "305"),
        
        # 6-Man Raft packages
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="6-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="1"), Price = "165"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="6-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="2"), Price = "180"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="6-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="3"), Price = "187"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="6-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="4"), Price = "187"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="6-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="5"), Price = "193"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="6-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="6"), Price = "205"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="6-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="7"), Price = "337"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="6-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="7A"), Price = "367"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="6-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="8"), Price = "442"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="6-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="SP1"), Price = "172"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="6-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="SP2"), Price = "187"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="6-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="SP3"), Price = "187"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="6-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="SP4"), Price = "195"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="6-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="SP5"), Price = "367"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="6-Man Raft"), Trip = Trip_Detail.objects.get(Trip_Number="SP6"), Price = "457"),

        # Stand-Up Paddle Board packages
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Stand-Up Paddle Board"), Trip = Trip_Detail.objects.get(Trip_Number="1"), Price = "48"),
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Stand-Up Paddle Board"), Trip = Trip_Detail.objects.get(Trip_Number="2"), Price = "53"),

        # Tube packages
        Trip_Package(Water_Craft_Type = Water_Craft.objects.get(
            Type="Tube"), Trip = Trip_Detail.objects.get(Trip_Number="1"), Price = "25"),
    ])
