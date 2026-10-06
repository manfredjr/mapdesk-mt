use base::config::keys;
use hbb_common::config;

const APP_NAME: &str = "MapDesk-MT";
const SERVIDOR: &str = "rustdesk.manfred.com.br";
// Public key of the hbbs server, not a secret. The lab key comes in slice 2 and
// the production key in slice 5; the test fails while it is empty.
const CHAVE_PUBLICA: &str = "CIfvalwtUTbDkS3JePcW37QmphouWPv+Uewa1zRFdcs=";

// Runs before custom.txt is read, so a signed custom.txt still wins. Idempotent:
// the Flutter UI calls load_custom_client twice in the same process.
pub fn aplicar() {
    *config::APP_NAME.write().unwrap() = APP_NAME.to_owned();
    config::DEFAULT_SETTINGS
        .write()
        .unwrap()
        .insert(keys::OPTION_APPROVE_MODE.to_owned(), "click".to_owned());
    {
        let mut overwrite = config::OVERWRITE_SETTINGS.write().unwrap();
        overwrite.insert(keys::OPTION_ALLOW_AUTO_UPDATE.to_owned(), "N".to_owned());
        overwrite.insert(
            keys::OPTION_CUSTOM_RENDEZVOUS_SERVER.to_owned(),
            SERVIDOR.to_owned(),
        );
        overwrite.insert(keys::OPTION_KEY.to_owned(), CHAVE_PUBLICA.to_owned());
    }
    let mut builtin = config::BUILTIN_SETTINGS.write().unwrap();
    builtin.insert(keys::OPTION_REGISTER_DEVICE.to_owned(), "N".to_owned());
    builtin.insert(keys::OPTION_HIDE_POWERED_BY_ME.to_owned(), "Y".to_owned());
    builtin.insert(keys::OPTION_HIDE_SERVER_SETTINGS.to_owned(), "Y".to_owned());
}

#[cfg(test)]
mod tests {
    use base::config::keys;
    use hbb_common::{
        config::{self, Config, RENDEZVOUS_PORT},
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
        let rendezvous_server = Config::get_rendezvous_server();
        let auto_update = config::OVERWRITE_SETTINGS
            .read()
            .unwrap()
            .get(keys::OPTION_ALLOW_AUTO_UPDATE)
            .cloned();
        let key = config::OVERWRITE_SETTINGS
            .read()
            .unwrap()
            .get(keys::OPTION_KEY)
            .cloned();
        let powered_by = config::BUILTIN_SETTINGS
            .read()
            .unwrap()
            .get(keys::OPTION_HIDE_POWERED_BY_ME)
            .cloned();
        let hide_server = config::BUILTIN_SETTINGS
            .read()
            .unwrap()
            .get(keys::OPTION_HIDE_SERVER_SETTINGS)
            .cloned();

        *config::APP_NAME.write().unwrap() = "RustDesk".to_owned();
        config::DEFAULT_SETTINGS
            .write()
            .unwrap()
            .remove(keys::OPTION_APPROVE_MODE);
        {
            let mut overwrite = config::OVERWRITE_SETTINGS.write().unwrap();
            overwrite.remove(keys::OPTION_ALLOW_AUTO_UPDATE);
            overwrite.remove(keys::OPTION_CUSTOM_RENDEZVOUS_SERVER);
            overwrite.remove(keys::OPTION_KEY);
        }
        {
            let mut builtin = config::BUILTIN_SETTINGS.write().unwrap();
            builtin.remove(keys::OPTION_REGISTER_DEVICE);
            builtin.remove(keys::OPTION_HIDE_POWERED_BY_ME);
            builtin.remove(keys::OPTION_HIDE_SERVER_SETTINGS);
        }

        assert_eq!(app_name, "MapDesk-MT");
        assert_eq!(approve_mode, ApproveMode::Click);
        assert!(no_register_device);
        assert_eq!(api_server, "");
        assert_eq!(auto_update.as_deref(), Some("N"));
        assert_eq!(powered_by.as_deref(), Some("Y"));
        assert_eq!(
            rendezvous_server,
            format!("rustdesk.manfred.com.br:{RENDEZVOUS_PORT}")
        );
        assert_eq!(key.as_deref(), Some(super::CHAVE_PUBLICA));
        assert!(!super::CHAVE_PUBLICA.is_empty());
        assert_eq!(hide_server.as_deref(), Some("Y"));
    }
}
