use base::config::keys;
use hbb_common::config;

const APP_NAME: &str = "MapDesk-MT";

// Runs before custom.txt is read, so a signed custom.txt still wins. Idempotent:
// the Flutter UI calls load_custom_client twice in the same process.
pub fn aplicar() {
    *config::APP_NAME.write().unwrap() = APP_NAME.to_owned();
    config::DEFAULT_SETTINGS
        .write()
        .unwrap()
        .insert(keys::OPTION_APPROVE_MODE.to_owned(), "click".to_owned());
    config::OVERWRITE_SETTINGS
        .write()
        .unwrap()
        .insert(keys::OPTION_ALLOW_AUTO_UPDATE.to_owned(), "N".to_owned());
    let mut builtin = config::BUILTIN_SETTINGS.write().unwrap();
    builtin.insert(keys::OPTION_REGISTER_DEVICE.to_owned(), "N".to_owned());
    builtin.insert(keys::OPTION_HIDE_POWERED_BY_ME.to_owned(), "Y".to_owned());
}

#[cfg(test)]
mod tests {
    use base::config::keys;
    use hbb_common::{
        config::{self, Config},
        password_security::{self, ApproveMode},
    };

    // A single test on purpose: it changes process-wide tables, and the end of the
    // test puts them back so other tests in the same binary are not affected.
    #[test]
    fn aplicar_define_nome_e_padroes_da_mt() {
        super::aplicar();
        super::aplicar();

        let app_name = config::APP_NAME.read().unwrap().clone();
        let approve_mode = password_security::approve_mode();
        let no_register_device = Config::no_register_device();
        let api_server = crate::common::get_api_server(String::new(), String::new());
        let auto_update = config::OVERWRITE_SETTINGS
            .read()
            .unwrap()
            .get(keys::OPTION_ALLOW_AUTO_UPDATE)
            .cloned();
        let powered_by = config::BUILTIN_SETTINGS
            .read()
            .unwrap()
            .get(keys::OPTION_HIDE_POWERED_BY_ME)
            .cloned();

        *config::APP_NAME.write().unwrap() = "RustDesk".to_owned();
        config::DEFAULT_SETTINGS
            .write()
            .unwrap()
            .remove(keys::OPTION_APPROVE_MODE);
        config::OVERWRITE_SETTINGS
            .write()
            .unwrap()
            .remove(keys::OPTION_ALLOW_AUTO_UPDATE);
        {
            let mut builtin = config::BUILTIN_SETTINGS.write().unwrap();
            builtin.remove(keys::OPTION_REGISTER_DEVICE);
            builtin.remove(keys::OPTION_HIDE_POWERED_BY_ME);
        }

        assert_eq!(app_name, "MapDesk-MT");
        assert_eq!(approve_mode, ApproveMode::Click);
        assert!(no_register_device);
        assert_eq!(api_server, "");
        assert_eq!(auto_update.as_deref(), Some("N"));
        assert_eq!(powered_by.as_deref(), Some("Y"));
    }
}
