import 'package:flutter/material.dart';
import 'package:flutter_hbb/mt/mt_info.dart';
import 'package:url_launcher/url_launcher_string.dart';

class MtLogoLink extends StatelessWidget {
  final double altura;

  const MtLogoLink({Key? key, this.altura = 64}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Tooltip(
      message:
          'MT - Manfred Tecnologia: abre o site www.manfred.com.br no navegador',
      child: Semantics(
        label: 'MT - Manfred Tecnologia',
        button: true,
        child: MouseRegion(
          cursor: SystemMouseCursors.click,
          child: InkWell(
            mouseCursor: SystemMouseCursors.click,
            onTap: () => launchUrlString(kMtSiteMarca),
            child: Image.asset(
              'assets/mt-logo.png',
              height: altura,
              filterQuality: FilterQuality.high,
            ),
          ),
        ),
      ),
    );
  }
}
