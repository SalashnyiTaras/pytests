class TestUser:
    """writing tests using pytest factories"""
    def test_user_first_name(self, new_user):
        assert new_user.first_name == 'tarik-salik'

    def test_change_user_first_name(self, new_user):
        new_user.first_name = 'Taras'
        assert new_user.first_name == 'Taras'

    def test_user_username(self, new_user):
        assert new_user.username == 'Tarik'

    def test_change_user_username(self, new_user):
        new_user.username = 'Marik'
        assert new_user.username == 'Marik'

    def test_user_password(self, new_user):
        assert new_user.check_password('password')

    def test_change_user_password(self, new_user):
        new_user.set_password('9379992www')
        assert new_user.check_password('9379992www')

    def test_user_set_user_is_active(self, new_user):
        new_user.is_active = True
        assert new_user.is_active
        new_user.is_active = False
        assert not new_user.is_active

    def test_user_set_user_is_staff(self, new_user):
        new_user.is_staff = True
        assert new_user.is_staff
        new_user.is_staff = False
        assert not new_user.is_staff

    def test_user_set_user_is_superuser(self, new_user):
        new_user.is_superuser = True
        assert new_user.is_superuser
        new_user.is_superuser = False
        assert not new_user.is_superuser


class TestStaffUser:
    def test_staff_user_first_name(self, new_staff_user):
        assert new_staff_user.first_name == 'tarik-salik'

    def test_staff_username(self, new_staff_user):
        assert new_staff_user.username == 'Tarik'

    def test_staff_user_password(self, new_staff_user):
        assert new_staff_user.check_password('password') is True

    def test_user_is_staff(self, new_staff_user):
        assert new_staff_user.is_staff


class TestSuperuser:
    def test_staff_user_first_name(self, new_super_user):
        assert new_super_user.first_name == 'tarik-salik'

    def test_staff_username(self, new_super_user):
        assert new_super_user.username == 'password'

    def test_staff_user_password(self, new_super_user):
        assert new_super_user.check_password('Tarik') is True

    def test_user_is_staff(self, new_super_user):
        assert new_super_user.is_staff




