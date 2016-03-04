#! env python

import sys
import os
import xml.etree.ElementTree
from termcolor import colored

class HadoopConfComparator(object):
    def __init__(self):
        pass

    @staticmethod
    def compare_two_hadoop_conf_dir(conf_dir_1, conf_dir_2):
        conf_1 = HadoopConfComparator.read_hadoop_conf_dir(conf_dir_1)
        conf_2 = HadoopConfComparator.read_hadoop_conf_dir(conf_dir_2)
        (added, removed, modified, same) = HadoopConfComparator.dict_compare(conf_1, conf_2)

        HadoopConfComparator.print_header("Added configuration:")
        for key in added:
            HadoopConfComparator.print_kv(key, conf_2[key])

        HadoopConfComparator.print_header("\nRemoved configuration, with old values:")
        for key in removed:
            HadoopConfComparator.print_kv(key, conf_1[key])

        HadoopConfComparator.print_header("\nModified configuration:")
        for key in modified:
            print(colored(key + ":\n", 'blue', attrs = ['bold']) + colored(conf_1[key], 'green') + "\n" + colored(conf_2[key], 'red'))

    @staticmethod
    def print_header(str):
        print(colored(str + "\n", 'red', attrs=['underline', 'bold']))

    @staticmethod
    def print_kv(key, value):
        print(colored(key + " : ", 'cyan') + colored(value, 'green'))


    @staticmethod
    def read_hadoop_conf_dir(conf_dir):
        configuration = {}
        for conf_file_name in os.listdir(conf_dir):
            if conf_file_name.endswith(".xml"):
                more_conf = HadoopConfComparator.read_hadoop_conf_xml_file(conf_dir + "/" + conf_file_name)
                configuration.update(more_conf)
        return configuration

    @staticmethod
    def read_hadoop_conf_xml_file(xml_file):
        configuration = {}
        e = xml.etree.ElementTree.parse(xml_file).getroot()
        for property in e.findall('property'):
            name = property.findall('name')[0].text
            value = property.findall('value')[0].text
            configuration[name] = value
        return configuration

    @staticmethod
    def dict_compare(d1, d2):
        d1_keys = set(d1.keys())
        d2_keys = set(d2.keys())
        intersect_keys = d1_keys.intersection(d2_keys)
        added = d2_keys - d1_keys
        removed = d1_keys - d2_keys
        modified = {o : (d2[o], d1[o]) for o in intersect_keys if d2[o] != d1[o]}
        same = set(o for o in intersect_keys if d2[o] == d1[o])
        return added, removed, modified, same


if __name__ == '__main__':

    if len(sys.argv) is not 3:
        print "Need two arguments: <base-conf> <new-conf>"
        sys.exit(1)

    conf_dir_1 = sys.argv[1]
    conf_dir_2 = sys.argv[2]
    HadoopConfComparator().compare_two_hadoop_conf_dir(conf_dir_1, conf_dir_2)
