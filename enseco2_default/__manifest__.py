##############################################################################
#
#    Copyright (C) 2021  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   le agregamos esto
##############################################################################

{
    'name': 'enseco2',
    'version': '13.0.1.0.0',
    'category': 'Tools',
    'summary': 'Proyecto enseco',
    'author': 'SDH',
    'website': 'http://github.com/jobiols/cl-test',
    'license': 'AGPL-3',
    'depends': [
        ],
    'installable': True,

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    # Config to write in odoo.conf
    'config': [
        'limit_request': '8196',
        'limit_memory_soft': '640000000',
        'limit_memory_hard': '760000000',
        'limit_time_cpu': '60',
        'limit_time_real': '120',
    #'dbfilter': 'goldway',
        'workers = 6',
        'server_wide_modules = web,queue_job',
    ],

    'port': '8069',

    'git-repos': [
        'https://github.com/sistemasdehudson/cl-enseco2',
        'https://github.com/regaby/odoo-custom.git',
        ##'https://github.com/regaby/l10n_ar_fe_qr',
        ##'https://github.com/regaby/l10n_ar_fe_qr ctmil/l10n_ar_fe_qr',
        'https://github.com/regaby/sdeh-pos.git',
        'https://github.com/jobiols/odoo-addons.git',
        ## localización
        'https://github.com/ingadhoc/odoo-argentina.git',
        'https://github.com/ingadhoc/odoo-argentina-ce.git',
        'https://github.com/ingadhoc/argentina-sale.git',
        'https://github.com/ingadhoc/account-payment.git',
        'https://github.com/ingadhoc/account-invoicing.git',
        'https://github.com/ingadhoc/account-financial-tools.git',
        'https://github.com/ingadhoc/sale.git',
        'https://github.com/ingadhoc/stock.git',
        'https://github.com/ingadhoc/aeroo_reports.git',
        'https://github.com/ingadhoc/website.git',
        'https://github.com/OCA/account-financial-reporting.git',
        'https://github.com/OCA/reporting-engine.git',
        'https://github.com/OCA/server-ux.git',
        'https://github.com/OCA/mis-builder.git',
        'https://github.com/OCA/sale-workflow.git',
        'https://github.com/OCA/web.git',
        ##
        ##'https://github.com/ctmil/contract.git',
        #'https://github.com/CybroOdoo/CybroAddons.git',
        'https://github.com/itpp-labs/pos-addons.git',
        'https://github.com/odoomates/odooapps.git',
        ##
        'https://github.com/sistemasdehudson/sdehposaddons.git',
        ##
        ##'https://github.com/sistemasdehudson/zero_kitchen',
        ##'https://github.com/OCA/pos/tree/13.0',
        ##'https://github.com/OCA/pos.git',
        ##'https://github.com/oca/report-print-send/tree/13.0',
        ##'https://github.com/OCA/report-print-send.git',
        ##'https://github.com/pronexo-argentina/pos_proxy_services.git -b 13.0',
        'https://github.com/OCA/contract.git -b 13.0',
        'https://github.com/odoomates/odooapps.git -b 13.0',
        'https://github.com/OCA/project -b 13.0',
        'https://github.com/ingadhoc/purchase -b 13.0',
        'https://github.com/ingadhoc/product -b 13.0',
        'https://github.com/ingadhoc/website -b 13.0',
        'https://github.com/OCA/project-reporting -b 13.0',
        'https://github.com/OCA/purchase-workflow -b 13.0',
        ##
        'https://github.com/filoquin/odoo_retail -b 13.0',
        'https://github.com/OCA/queue -b 13.0',
        'https://github.com/OCA/e-commerce -b 13.0',
        'https://github.com/OCA/hr-attendance.git  -b 13.0',
        'https://github.com/OCA/social.git -b 13.0',
        'https://github.com/OCA/helpdesk -b 13.0',
        'https://github.com/OCA/management-system -b 13.0',
        'https://github.com/OCA/knowledge -b 13.0',
        'https://github.com/OCA/bank-statement-import -b 13.0',
         ##modulos stock para remito
        'https://github.com/OCA/stock-logistics-workflow.git -b 13.0',
    ],
    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo regaby/odoo-ce:13.0',
        'postgres postgres:10.1-alpine',
    ]
}
