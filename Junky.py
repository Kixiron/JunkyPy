import os
import random
import string
import time

class Junky():
    def __init__(self, path, file, rejunk):
        self.file = os.path.join(path + '\\' + file)
        self.filename = file
        self.rejunk = rejunk

    def junkify(self):
        file = open(self.file, "r")
        file_raw = file.readlines()
        file.close()
        delete = junk_token = skip_file = False
        new_file = []
        for line in file_raw:
            line = line.strip()
            if line == "/* SKIP FILE */":
                skip_file = True
                break
            elif line == "/* This file has been junkified by JunkyPy */":
                junk_token = True
            elif line == "/* INSERT JUNK FUNCTION */":
                new_file.append(self.generate_function())
            elif line == "/* INSERT JUNK CLASS */":
                new_file.append(self.generate_class())
            elif line == "/* INSERT JUNK PRIVATE VARIABLES */":
                new_file.append(self.generate_private_vars())
            elif line == "/* INSERT JUNK IMPORTS */":
                new_file.append(self.generate_imports())
            elif line == "/* START JUNK */":
                delete = True
            elif line == "/* END JUNK FUNCTION */":
                new_file.append("/* INSERT JUNK FUNCTION */")
                delete = False
            elif line == "/* END JUNK CLASS */":
                new_file.append("/* INSERT JUNK CLASS */")
                delete = False
            elif line == "/* END JUNK PRIVATE VARS */":
                new_file.append("/* INSERT JUNK PRIVATE VARIABLES */")
                delete = False
            elif line == "/* END JUNK IMPORTS */":
                new_file.append("/* INSERT JUNK IMPORTS */")
                delete = False
            else:
                if delete == False:
                    new_file.append(line)
        if skip_file:
            return "Skipped File {}".format(self.file)
            pass
        else:
            if junk_token == False:
                new_file.insert(0, "/* This file has been junkified by JunkyPy */")
                return_msg = "Junked File {}".format(self.filename)
            else:
                return_msg = "Un-junked File {}".format(self.filename)
            file = open(self.file, "w")
            file.close()
            file = open(self.file, "w")
            file.write('\n'.join(new_file).replace("}}", "}").replace("{{", "{"))
            file.close()
            if self.rejunk and junk_token:
                self.junkify_safe()
                return_msg = "Un-junked and re-junked {}".format(self.filename)
            return return_msg

    def junkify_safe(self):
        file = open(self.file, "r")
        file_raw = file.readlines()
        file.close()
        junk_token = skip_file = False
        new_file = []
        for line in file_raw:
            line = line.strip()
            if line == "/* This file has been junkified by JunkyPy */":
                junk_token = True
            elif line == "/* INSERT JUNK FUNCTION */":
                new_file.append(self.generate_function())
            elif line == "/* INSERT JUNK CLASS */":
                new_file.append(self.generate_class())
            elif line == "/* INSERT JUNK PRIVATE VARIABLES */":
                new_file.append(self.generate_private_vars())
            elif line == "/* INSERT JUNK IMPORTS */":
                new_file.append(self.generate_imports())
            else:
                new_file.append(line)
        else:
            if junk_token == False:
                new_file.insert(0, "/* This file has been junkified by JunkyPy */")
            file = open(self.file, "w")
            file.close()
            file = open(self.file, "w")
            file.write('\n'.join(new_file).replace("}}", "}").replace("{{", "{"))
            file.close()

    def generate_class(self):
        junk = "/* START JUNK */\n"
        junk += "private class {}_class\n".format(self.generate_var())
        junk += "{{\n"
        for i in range(random.randint(1, 3)):
            junk += self.generate_global_var()
        for i in range(random.randint(1, 3)):
            junk += self.generate_enum()
        for i in range(random.randint(1, 2)):
            junk += self.generate_class_function()
        junk += "}}\n"
        junk += "/* END JUNK CLASS */"
        return junk

    def generate_class_function(self):
        junk = "private async void {}_func()\n".format(self.generate_var())
        junk += "{{\n"
        for i in range(random.randint(1, 3)):
            junk += self.generate_if()
        for i in range(random.randint(0, 2)):
            junk += self.generate_for()
        junk += "}}\n"
        return junk

    def generate_function(self):
        junk = "/* START JUNK */\n"
        junk += "private async void {}_func()\n".format(self.generate_var())
        junk += "{{\n"
        for i in range(random.randint(1, 3)):
            junk += self.generate_if()
        for i in range(random.randint(0, 3)):
            junk += self.generate_for()
        junk += "}}\n"
        junk += "/* END JUNK FUNCTION */"
        return junk

    def generate_imports(self):
        imports = [ "System", "System.CodeDom", "System.Collections", "System.ComponentModel", "System.Configuration", "System.Deployment", "System.Diagnostics", "System.Diagnostics.CodeAnalysis", "System.Diagnostics.Contracts", "System.Diagnostics.Eventing", "System.Diagnostics.Tracing", "System.Diagnostics.PreformanceData", "System.Dynamic", "System.Globalization", "System.IO", "System.Linq", "System.Management", "System.Media", "System.Net", "System.Reflection", "System.Timers","System.Timers","System.Threading","System.Text","System.Text.RegularExpressions", "System.Security", "System.Runtime", "System.Resources", "System.Windows" ]
        junk = "/* START JUNK */\n"
        for i in range(random.randint(1, 5)):
            junk += "using " + random.choice(imports) + ";\n"
        junk += "/* END JUNK IMPORTS */"
        return junk

    def generate_if(self):
        operand_types = [ "==", "<=", ">=", ">", "<", "!=" ]
        conditionals = [ "&&", "||" ]
        values = [ "int", "uint", "long", "ulong", "byte", "short", "bool" ]
        condition = ""
        for i in range(random.randint(1, 3)):
            condition += " ({} {} {}) ".format(self.generate_ulong(), random.choice(operand_types), self.generate_ulong())
        condition = condition.replace("  ", " " + random.choice(conditionals) + " ").strip()
        junk = "if ({})".format(condition)
        junk += "{{\n"
        for i in range(random.randint(1, 4)):
            value = random.choice(values)
            if value == "int":
                junk += "{} {} = {};\n".format(value, self.generate_var() , self.generate_int())
            elif value == "uint":
                junk += "{} {} = {};\n".format(value, self.generate_var() , self.generate_uint())
            elif value == "long":
                junk += "{} {} = {};\n".format(value, self.generate_var() , self.generate_long())
            elif value == "ulong":
                junk += "{} {} = {};\n".format(value, self.generate_var() , self.generate_ulong())
            elif value == "byte":
                junk += "{} {} = {};\n".format(value, self.generate_var() , self.generate_byte())
            elif value == "short":
                junk += "{} {} = {};\n".format(value, self.generate_var() , self.generate_short())
            elif value == "bool":
                junk += "{} {} = {};\n".format(value, self.generate_var() , self.generate_bool())
        for i in range(random.randint(0, 2)):
            junk += self.generate_safe_for()
        junk += "}}\n"
        return junk

    def generate_safe_if(self):
        operand_types = [ "==", "<=", ">=", ">", "<", "!=" ]
        conditionals = [ "&&", "||" ]
        values = [ "int", "uint", "long", "ulong", "byte", "short", "bool" ]
        condition = ""
        for i in range(random.randint(1, 4)):
            condition += " ({} {} {}) ".format(self.generate_ulong(), random.choice(operand_types), self.generate_ulong())
        condition = condition.replace("  ", " " + random.choice(conditionals) + " ").strip()
        junk = "if ({})".format(condition)
        junk += "{{\n"
        for i in range(random.randint(1, 4)):
            value = random.choice(values)
            if value == "int":
                junk += "{} {} = {};\n".format(value, self.generate_var() , self.generate_int())
            elif value == "uint":
                junk += "{} {} = {};\n".format(value, self.generate_var() , self.generate_uint())
            elif value == "long":
                junk += "{} {} = {};\n".format(value, self.generate_var() , self.generate_long())
            elif value == "ulong":
                junk += "{} {} = {};\n".format(value, self.generate_var() , self.generate_ulong())
            elif value == "byte":
                junk += "{} {} = {};\n".format(value, self.generate_var() , self.generate_byte())
            elif value == "short":
                junk += "{} {} = {};\n".format(value, self.generate_var() , self.generate_short())
            elif value == "bool":
                junk += "{} {} = {};\n".format(value, self.generate_var() , self.generate_bool())
        junk += "}}\n"
        return junk

    def generate_for(self):
        operand_types = [ "<=", ">=", ">", "<" ]
        for_var = self.generate_var()
        junk = "for (var {} = 0; {} {} {}; {}++)\n".format(for_var, for_var, random.choice(operand_types), self.generate_ulong(), for_var)
        junk += "{{\n"
        for i in range(random.randint(1, 3)):
            junk += self.generate_if()
        junk += "}}\n"
        return junk

    def generate_safe_for(self):
        operand_types = [ "<=", ">=", ">", "<" ]
        for_var = self.generate_var()
        junk = "for (var {} = 0; {} {} {}; {}++)\n".format(for_var, for_var, random.choice(operand_types), self.generate_ulong(), for_var)
        junk += "{{\n"
        for i in range(random.randint(1, 2)):
            junk += self.generate_safe_if()
        junk += "}}\n"
        return junk

    def generate_enum(self):
        values = [ "int", "uint", "long", "ulong", "byte", "short", "bool" ]
        junk = "[Flags]\n"
        value = random.choice(values)
        junk += "private enum {}_enum : {}\n".format(self.generate_var(), value)
        junk += "{{\n"
        for i in range(random.randint(1, 10)):
            if value == "int":
                generator = self.generate_int()
            elif value == "uint":
                generator = self.generate_uint()
            elif value == "long":
                generator = self.generate_long()
            elif value == "ulong":
                generator = self.generate_ulong()
            elif value == "byte":
                generator = self.generate_byte()
            elif value == "short":
                generator = self.generate_short()
            elif value == "bool":
                generator = self.generate_bool()
            junk += "{} = {},\n".format(self.generate_var(), generator)
        junk += "}}\n"
        return junk

    def generate_private_vars(self):
        junk = "/* START JUNK */\n"
        for i in range(random.randint(1, 7)):
            junk += self.generate_global_var()
        junk += "/* END JUNK PRIVATE VARS */\n"
        return junk

    def generate_global_var(self):
        var_types = [ "string", "string[]", "int", "int[]", "long", "long[]", "ulong", "ulong[]", "UIntPtr", "UIntPtr[]", "IntPtr", "IntPtr[]" "bool", "bool[]", "var", "var[]" "sbyte", "sbyte[]", "short", "short[]", "byte", "byte[]", "ushort", "ushort[]", "uint", "uint[]", "char", "char[]", "float", "float[]", "double", "double[]", "decimal", "decimal[]", "object",  "object[]" ]
        value = random.choice(var_types)
        if value == "int":
            return "private static {} {} = {};\n".format(value, self.generate_var() , self.generate_int())
        elif value == "uint":
            return "private static {} {} = {};\n".format(value, self.generate_var() , self.generate_uint())
        elif value == "long":
            return "private static {} {} = {};\n".format(value, self.generate_var() , self.generate_long())
        elif value == "ulong":
            return "private static {} {} = {};\n".format(value, self.generate_var() , self.generate_ulong())
        elif value == "byte":
            return "private static {} {} = {};\n".format(value, self.generate_var() , self.generate_byte())
        elif value == "short":
            return "private static {} {} = {};\n".format(value, self.generate_var() , self.generate_short())
        elif value == "bool":
            return "private static {} {} = {};\n".format(value, self.generate_var() , self.generate_bool())
        else:
            return "private static {} {};\n".format(value, self.generate_var())

    def generate_var(self):
        return ''.join([random.choice(string.ascii_letters) for n in range(random.randint(5, 50))])

    def generate_int(self):
        return random.randint(-2147483647, 2147483647)

    def generate_uint(self):
        return random.randint(-4294967295, 4294967295)

    def generate_long(self):
        return random.randint(-9223372036854775807, 9223372036854775807)

    def generate_ulong(self):
        return random.randint(-18446744073709551615, 18446744073709551615)

    def generate_byte(self):
        return random.randint(0, 255)

    def generate_short(self):
        return random.randint(-32768, 32768)

    def generate_bool(self):
        return random.choice([ "true", "false", "null" ])

def main():
    path = input("File Directory:\n")
    if os.path.exists(path) == False:
        print("That isn't a valid path")
        exit()
    rejunk = False
    rejunk_string = input("Do you want to re-junk already junked files? [yes/no]\n")
    if rejunk_string.lower().strip() == "yes" or rejunk_string.lower().strip() == "y":
        rejunk = True
        print("Files will be re-junked")
    else:
        rejunk = False
        print("Files will not be re-junked")
    file_list = []
    random.seed()
    for file in os.listdir(path):
        if file.endswith(".cs"):
            if file.endswith(".csproj"):
                pass
            file_list.append(file)
            if len(file_list) == 1:
                print("{} file found".format(len(file_list)))
            elif len(file_list) < 0:
                print("No files found, quitting")
                exit()
            else:
                print("{} files found".format(len(file_list)))
    for file in file_list:
        junker = Junky(path, file, rejunk)
        status = junker.junkify()
        print(status)

main()
