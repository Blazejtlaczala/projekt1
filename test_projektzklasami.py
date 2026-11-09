from projektzklasami import Angle


def test_pass():
    assert 2 == 2


def test_addition():
    assert 2 + 2 == 4


def test_modulo():
    assert -10 % 60 == 50


def test_dzielenie():
    assert -10 // 60 == -1


def test_angle_creation():
    angle = Angle(30, 15, 50)
    assert angle.grades == 30
    assert angle.minutes == 15
    assert angle.seconds == 50


def test_angle_creation_negative():
    angle = Angle(-30, 15, 50)
    assert angle.grades == -30
    assert angle.minutes == 15
    assert angle.seconds == 50


def test_to_seconds_typical():
    angle = Angle(30, 15, 50)
    assert angle.to_seconds() == 108950


def test_to_seconds_negative():
    angle = Angle(-30, 15, 50)
    assert angle.to_seconds() == -108950


def test_to_seconds_borders():
    angle = Angle(0, 0, 0)
    assert angle.to_seconds() == 0
    angle = Angle(360, 0, 0)
    assert angle.to_seconds() == 0
    angle = Angle(-360, 0, 0)
    assert angle.to_seconds() == 0


def test_to_seconds_notcorrect():
    angle = Angle(30, 15, -50)
    assert angle.to_seconds() == 108850


def test_from_seconds_typical():
    angle = Angle.from_seconds(108950)
    assert angle.grades == 30
    assert angle.minutes == 15
    assert angle.seconds == 50


def test_from_seconds_borders():
    angle = Angle.from_seconds(0)
    assert angle.grades == 0
    assert angle.minutes == 0
    assert angle.seconds == 0
    angle = Angle.from_seconds(1296000)
    assert angle.grades == 0
    assert angle.minutes == 0
    assert angle.seconds == 0
    angle = Angle.from_seconds(-1296000)
    assert angle.grades == 0
    assert angle.minutes == 0
    assert angle.seconds == 0


def test_from_seconds_negative():
    angle = Angle.from_seconds(-108950)
    assert angle.grades == -30
    assert angle.minutes == 15
    assert angle.seconds == 50


def test_from_seconds_large():
    angle = Angle.from_seconds(2592060)
    assert angle.grades == 0
    assert angle.minutes == 1
    assert angle.seconds == 0


def test_print_angle():
    angle = Angle(30, 15, 50)
    assert str(angle) == "30° 15' 50''"


def test_print_angle_negative():
    angle = Angle(-30, 15, 50)
    assert str(angle) == "-30° 15' 50''"


def test_print_angle_borders():
    angle = Angle(0, 0, 0)
    assert str(angle) == "0° 00' 00''"
    angle = Angle(360, 0, 0)
    assert str(angle) == "0° 00' 00''"
    angle = Angle(-0, 0, 0)
    assert str(angle) == "0° 00' 00''"


def test_angle_grades():
    angle = Angle(grades=30)
    assert angle.grades == 30
    assert angle.minutes == 0
    assert angle.seconds == 0


def test_angle_minutes():
    angle = Angle(minutes=15)
    assert angle.grades == 0
    assert angle.minutes == 15
    assert angle.seconds == 0


def test_angle_seconds():
    angle = Angle(seconds=50)
    assert angle.grades == 0
    assert angle.minutes == 0
    assert angle.seconds == 50


def test_angle_minutes_large():
    angle = Angle(minutes=61)
    assert angle.grades == 1
    assert angle.minutes == 1
    assert angle.seconds == 0


def test_angle_seconds_large():
    angle = Angle(seconds=3666)
    assert angle.grades == 1
    assert angle.minutes == 1
    assert angle.seconds == 6


def test_1_z_projektu_tworzenie_kątów():
    angle1 = Angle(30, 45, 50)  # 30 stopni, 45 minut, 50 sekund
    angle2 = Angle(15, 20, 25)  # 15 stopni, 20 minut, 25 sekund
    assert angle1.grades == 30
    assert angle1.minutes == 45
    assert angle1.seconds == 50
    assert angle2.grades == 15
    assert angle2.minutes == 20
    assert angle2.seconds == 25


def test_2_z_projektu_dodawanie_kątów():
    angle1 = Angle(30, 45, 50)  # 30 stopni, 45 minut, 50 sekund
    angle2 = Angle(15, 20, 25)  # 15 stopni, 20 minut, 25 sekund
    result_angle = angle1 + angle2
    assert result_angle.grades == 46
    assert result_angle.minutes == 6
    assert result_angle.seconds == 15
    assert str(result_angle) == "46° 06' 15''"
    assert angle1.to_seconds() == 110750

def test_3_z_projektu_odejmowanie_kątów():
    angle1 = Angle(30, 45, 50)  # 30 stopni, 45 minut, 50 sekund
    angle2 = Angle(15, 20, 25)  # 15 stopni, 20 minut, 25 sekund
    result_angle = angle1 - angle2
    assert result_angle.grades == 15
    assert result_angle.minutes == 25
    assert result_angle.seconds == 25


def test_4_z_projektu_porównywanie_kątów_równość():
    angle1 = Angle.from_seconds(5400)
    assert angle1 == Angle(minutes=90)

def test_5_z_projektu_porównywanie_kątów_mniejszość():
    angle1 = Angle.from_seconds(5400)
    assert angle1 < Angle(minutes=91)

def test_6_z_projektu_porównywanie_kątów_większość():
    angle1 = Angle.from_seconds(5400)
    assert (angle1 > Angle(minutes=89))

def test_7_z_projektu_porównywanie_kątów_mniejsze_równe():
    angle1 = Angle.from_seconds(5400)
    assert (angle1 <= Angle(minutes=90))
    assert (angle1 >= Angle(minutes=90))
