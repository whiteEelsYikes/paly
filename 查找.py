import os
import shutil


class Verify_init:

    def __init__(self):
        self.verify_content = r''
        self.verify_source = r''
        self.path = r''
        self.path_file = r''
        self.verify_path_tuple = None
        self.dispose_rename_file_name = f'{self.verify_source}'
        # self.verify_not_folder = None
        # self.verify_empty_file = None
        self.dispose_remove_file_mode = True
        self.dispose_rename_file_mode = True
        self.verify_blur_mode = True

    def get_initial_data(self, verify_content_path, verify_source_path=r'E:\数据库\verify_source_data.db',
                         db_reservoir='Verify', db_table='', db_field='verify'):
        pass

    def verify(self):
        self._dispose_path_file_update()
        if self.verify_blur_mode:
            if self.verify_content.find(self.verify_source) != -1:
                return (self.verify_content, self.verify_source)

        elif not self.verify_blur_mode:
            if self.verify_content == self.verify_source:
                return (self.verify_content, self.verify_source,)

    def _dispose_path_file_update(self):
        if self.path.find('/') == 1:
            self.path_file = f'{self.path}/{self.verify_content}'
        elif self.path.find('\\'):
            self.path_file = f'{self.path}\\{self.verify_content}'

    def dispose_not_folder(self):
        if os.path.isfile(self.path_file):
            # self.verify_content.remove(self.path_file)
            # self.verify_not_folder.append(self.path_file)
            return True

    def dispose_empty_file(self):
        if not os.path.getsize(self.path_file):
            # self.verify_content.remove(self.path_file)
            # self.verify_empty_file.append(self.path_file)
            return True

    def dispose_remove_file(self):
        if self.dispose_remove_file_mode:
            shutil.rmtree(self.path_file)
        elif not self.dispose_remove_file_mode:
            os.remove(self.path_file)
        # try:
        #     self.verify_empty_file.remove(path_file)
        # except ValueError as err:
        #     self.verify_not_folder.remove(path_file)

    def dispose_rename_file(self):
        if self.dispose_rename_file_mode:
            os.rename(self.path_file, self.dispose_rename_file_name)
        elif not self.dispose_rename_file_mode:
            os.renames(self.path_file,
                       self.dispose_rename_file_name + os.path.splitext(self.verify_content)[-1])

    def dispose_(self):
        pass


class Verify_main:

    def __init__(self):
        self.verify_init = Verify_init()
        self.path = ''
        self.verify_content = []
        self.verify_source = []
        self.verify_succeed = []
        self.verify_fail = []
        self.verify_not_folder = None
        self.verify_empty_file = None
        self.verify_init_verify_key = None

        self.path_file_update_switch = None
        self.dispose_not_folder_switch = None
        self.dispose_empty_file_switch = None
        self.dispose_remove_file_switch = None
        self.dispose_rename_file_switch = None

    def dispose_apply_init(self):
        '''
        这个函数 可以使用，其他的没测试
        :return:
        '''
        self.dispose_apply_verify(0)
        for verify_source_item in self.verify_source:
            basis = 0
            self.verify_init.verify_source = verify_source_item
            while True:
                self.verify_init.verify_content = self.verify_content[basis]
                self.verify_init_verify_key = self.verify_init.verify()
                if self.verify_init_verify_key:
                    self.verify_succeed.append(verify_source_item)
                    self.dispose_apply_verify(1)
                    break

                if basis + 1 == len(self.verify_content):
                    self.verify_fail.append(verify_source_item)
                    self.dispose_apply_verify(-1)
                    break
                basis += 1
        return self.verify_succeed, self.verify_fail


    def dispose_apply_verify(self, verify_mode):
        if verify_mode == 0 :
            for item in self.verify_content:
                if self.dispose_not_folder_switch:
                    self.verify_init.path_file = f'{self.path}\\{item}'
                    self.verify_init.dispose_not_folder()
                if self.dispose_empty_file_switch:
                    self.verify_init.dispose_empty_file()
        elif verify_mode == 1 :
            if self.dispose_rename_file_switch:
                self.verify_init.dispose_rename_file()
        elif verify_mode == -1 :
            if self.dispose_remove_file_switch:
                self.verify_init.dispose_remove_file()

    def _dispose_path_file_update(self):
        if self.path.find('/') == 1:
            self.path_file = f'{self.path}/{self.verify_content}'
        elif self.path.find('\\'):
            self.path_file = f'{self.path}\\{self.verify_content}'

v = Verify_main()
a = ['a', 'b', 'c', 'd']
b = ['r', 't', 'y', 'a', 'b', 'c']
v.verify_content = b
v.verify_source = a
v.dispose_apply_init()
print()
print('================================')
print('v.verify_source:',v.verify_source)
print('v.verify_content:',v.verify_content)
print('v.verify_succeed:',v.verify_succeed)
print('v.verify_fail:',v.verify_fail)

