import eel
import math as m
import xlsxwriter
import random
eel.init('web')

details = {}
data = {}
final_data = []
summations = []

@eel.expose
def addLine(line_name, length, azimuth_degree, azimuth_minutes, azimuth_seconds):
    try:
        length = float(length)
        azimuth_degree = int(azimuth_degree)
        azimuth_minutes = int(azimuth_minutes)
        azimuth_seconds = float(azimuth_seconds)
    except:
        return "error"
    details[line_name] = [length, azimuth_degree, azimuth_minutes, azimuth_seconds]
    azimuth_degree *= (m.pi / 180)
    azimuth_minutes *= (m.pi / 180)
    azimuth_seconds *= (m.pi / 180)
    vertical_compound = length * (m.cos((((azimuth_seconds / 60) + azimuth_minutes) / 60) + azimuth_degree))
    horizontal_compound = length * (m.sin((((azimuth_seconds / 60) + azimuth_minutes) / 60) + azimuth_degree))
    data[line_name] = [round(vertical_compound, 6), round(horizontal_compound, 6)]

@eel.expose
def seeResult():
    vc_sum = sum([i[0] for i in data.values()])
    hc_sum = sum([i[1] for i in data.values()])
    unknownAngle = str(m.atan(abs(hc_sum/vc_sum)) * 180 / m.pi)
    if vc_sum > 0 and hc_sum > 0:
        unknownAngle = str(float(unknownAngle) + 180)
    if vc_sum < 0 and hc_sum > 0:
        unknownAngle = str(360 - float(unknownAngle))
    if vc_sum > 0 and hc_sum < 0:
        unknownAngle = str(180 - float(unknownAngle))
    degree = unknownAngle[:unknownAngle.index('.')]
    minutes = str(float("0." + unknownAngle[unknownAngle.index('.')+1:]) * 60)
    seconds = str(float("0." + minutes[minutes.index('.')+1:]) * 60)
    minutes = minutes[:minutes.index('.')]
    seconds = round(float(seconds), 2)
    finalLength = abs(vc_sum / m.cos(float(unknownAngle) * (m.pi / 180)))
    finalLength = round(finalLength, 3)
    name = int(ord(list(details.keys())[-1][-1]))
    name = chr(name) + list(details.keys())[0][0]


    final_data.append([name, finalLength, degree, minutes, seconds])

    degree = int(degree) * (m.pi / 180)
    minutes = int(minutes) * (m.pi / 180)
    seconds = float(seconds) * (m.pi / 180)
    finalLength = float(finalLength)
    vertical_compound = round(finalLength * m.cos((((seconds / 60) + minutes) / 60) + degree), 6)
    horizontal_compound = round(finalLength * m.sin((((seconds / 60) + minutes) / 60) + degree), 6)
    final_data.append([vertical_compound, horizontal_compound])
    vc_sum = round(sum([i[0] for i in data.values()]) + vertical_compound, 6)
    hc_sum = round(sum([i[1] for i in data.values()]) + horizontal_compound, 6)
    summations.append(vc_sum)
    summations.append(hc_sum)

    
    return (final_data, vc_sum, hc_sum)

@eel.expose
def getData():
    return [list(details.keys()), list(details.values()),  list(data.values())]

@eel.expose
def reset():
    global details, data, final_data, summations
    details = {}
    data = {}
    final_data = []
    summations = []

@eel.expose
def save(file_name, file_extension):
    if file_name == "":
        file_name = f"missing-side-length{random.randint(1, 999)}"
    workbook = xlsxwriter.Workbook(f'{file_name}.{file_extension}')

    worksheet = workbook.add_worksheet("Missing Side Length")
    
    row = 0
    
    worksheet.write(row, 0, "Line")
    worksheet.write(row, 1, "length")
    worksheet.write(row, 2, "degree")
    worksheet.write(row, 3, "minutes")
    worksheet.write(row, 4, "seconds")
    worksheet.write(row, 5, "Vl.C")
    worksheet.write(row, 6, "Hl.C")

    row += 1

    for k, v in details.items():
        worksheet.write(row, 0, k)
        worksheet.write(row, 1, v[0])
        worksheet.write(row, 2, v[1])
        worksheet.write(row, 3, v[2])
        worksheet.write(row, 4, v[3])
        worksheet.write(row, 5, data[k][0])
        worksheet.write(row, 6, data[k][1])
        row += 1
        
    
    worksheet.write(row, 0, final_data[0][0])
    worksheet.write(row, 1, final_data[0][1])
    worksheet.write(row, 2, final_data[0][2])
    worksheet.write(row, 3, final_data[0][3])
    worksheet.write(row, 4, final_data[0][4])
    worksheet.write(row, 5, final_data[1][0])
    worksheet.write(row, 6, final_data[1][1])

    worksheet.write(row + 1, 5, round(summations[0], 3))
    worksheet.write(row + 1, 6, round(summations[1], 3))




    
    workbook.close()

    

eel.start('index.html', size=(1140, 728))