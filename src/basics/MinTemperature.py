from mrjob.job import MRJob

class MrMinTemperature(MRJob):

    def MakeFahrenheit(self, tenthsOfCelsius):
        celsius = float(tenthsOfCelsius)/ 10.0
        fahrenheit = celsius * 1.8 + 32
        return fahrenheit

    def mapper(self, key, value):
        (loc, data, type, data, x,y,z,w)= value.split(',')
        if type == 'TMIN':
            temperature = self.MakeFahrenheit(data)
            yield loc, temperature

    def reducer(self, loc, temps):
        yield loc, min(temps)

if __name__ == '__main__':

    MrMinTemperature().run()